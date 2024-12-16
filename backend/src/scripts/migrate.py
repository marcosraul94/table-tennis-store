from src.utils.migration import MigrationTool

migration_tool = MigrationTool()


def lambda_handler(raw_event, context):
    migration_tool.migrate()


if __name__ == "__main__":
    migration_tool.migrate()
