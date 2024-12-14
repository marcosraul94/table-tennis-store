import os
from typing import Set
from boto3.dynamodb.conditions import Key
from importlib.util import spec_from_file_location, module_from_spec
from src.utils.constant import migrations_path
from src.utils.db import get_client
from src.utils.constant import dynamo_db_table_name


class MigrationTool:
    def __init__(self, dynamo_db_client=None):
        self.__dynamo_db_client = (
            dynamo_db_client if dynamo_db_client else get_client()
        )

    @property
    def __table(self):
        return self.__dynamo_db_client.Table(dynamo_db_table_name)

    @property
    def __migration_names_from_folder(self) -> Set[str]:
        return {
            migration_name.split(".")[0]
            for migration_name in os.listdir(migrations_path)
            if migration_name.endswith(".py")
        }

    @property
    def __migration_names_from_db(self) -> Set[str]:
        table_names = [
            table.table_name for table in self.__dynamo_db_client.tables.all()
        ]
        if dynamo_db_table_name not in table_names:
            return []

        response = self.__table.query(
            KeyConditionExpression=Key("pk").eq("MIGRATION#")
        )

        return {item["name"] for item in response.get("Items", [])}

    @property
    def __migration_names_to_execute(self) -> Set[str]:
        return self.__migration_names_from_folder.difference(
            self.__migration_names_from_db
        )

    @staticmethod
    def __import_migration_module(migration_name: str):
        module_path = os.path.join(migrations_path, f"{migration_name}.py")

        spec = spec_from_file_location(migration_name, module_path)
        module = module_from_spec(spec)
        spec.loader.exec_module(module)

        return module

    def __execute_migration_command(self, migration_name: str):
        migration_module = self.__import_migration_module(migration_name)

        print(f"Running {migration_name} migration...")
        migration_module.migrate()
        print(f"{migration_name} ran successfully!")

    def __save_migration_applied(self, migration_name: str):
        print(f"Saving {migration_name}...")
        self.__table.put_item(
            Item={
                "pk": "MIGRATION#",
                "sk": migration_name,
                "type": "MIGRATION",
                "name": migration_name,
            }
        )
        print(f"Migration {migration_name} saved correctly")

    def migrate(self):
        print("Migrations already applied:", self.__migration_names_from_db)
        print("Migrations from folder:", self.__migration_names_from_folder)
        print("Migrations to apply:", self.__migration_names_to_execute)

        if not self.__migration_names_to_execute:
            print("No migrations to apply found!")
            return

        for migration_name_to_execute in self.__migration_names_to_execute:
            self.__execute_migration_command(migration_name_to_execute)
            self.__save_migration_applied(migration_name_to_execute)


def lambda_handler(raw_event, context):
    migration_tool = MigrationTool()
    migration_tool.migrate()
