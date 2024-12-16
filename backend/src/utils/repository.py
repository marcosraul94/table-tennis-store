from typing import Union
import src.utils.db as dynamodb
from src.utils.entity import Entity
from src.utils.constant import dynamo_db_table_name
from src.utils.serialization import EntitySerialization


class Repository:
    EntitySerializationCls: EntitySerialization = EntitySerialization

    def __init__(
        self,
        client=dynamodb.get_client(),
        table_name=dynamo_db_table_name,
    ) -> None:
        self.__client = client
        self.__table_name = table_name

    @property
    def table(self):
        return self.__client.Table(self.__table_name)

    @classmethod
    def validate_item_found(cls, item: Union[dict, None]):
        if not item:
            raise Exception(f"{cls.entity.__class__.__name__} item not found!")

    def create(self, entity: Entity) -> None:
        self.create_all([entity])

    def create_all(self, entities: list[Entity]) -> None:
        with self.table.batch_writer() as batch:
            for entity in entities:
                item = self.EntitySerializationCls.to_item(entity)

                batch.put_item(Item={**item})

    def find_one(self, email: str) -> Entity:
        item = self.table.get_item(
            Key={
                "pk": self.create_pk(email),
                "sk": self.create_sk(email),
            }
        )
        self.validate_item_found(item)

        return self.EntitySerializationCls.to_entity(item)
