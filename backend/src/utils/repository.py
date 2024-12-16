import src.utils.db as dynamodb
from boto3.dynamodb.conditions import Key
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
        self.__table = None

    @property
    def table(self):
        if self.__table:
            return self.__table

        self.__table = self.__client.Table(self.__table_name)

        return self.__table

    def create(self, entities: list[Entity]) -> list[dict]:
        created_items = []

        with self.table.batch_writer() as batch:
            for entity in entities:
                item = self.EntitySerializationCls.to_item(entity)

                batch.put_item(Item={**item})
                created_items.append(item)

        return created_items

    def query_by_email(self, email: str) -> list[Entity]:
        pk = Key("pk").eq(self.EntitySerializationCls.create_pk(email))
        sk = Key("sk").eq(self.EntitySerializationCls.create_sk(email))

        response = self.table.query(KeyConditionExpression=pk & sk)

        return [
            self.EntitySerializationCls.to_entity(item)
            for item in response["Items"]
        ]
