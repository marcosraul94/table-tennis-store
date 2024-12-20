import json
from unittest import TestCase
from src.utils.app import create_app
from src.utils.repository import Repository


class FlaskClient:
    def __init__(self):
        self.__app = create_app()

    def post(self, route: str, body: dict):
        with self.__app.test_client() as client:
            return client.post(route, json=json.dumps(body)).get_json()


class E2ETestCase(TestCase):
    def setUp(self):
        table = Repository().table

        response = table.scan()
        items_to_delete = [
            item for item in response["Items"] if item["type"] != "Migration"
        ]

        with table.batch_writer() as batch:
            for item in items_to_delete:
                batch.delete_item(Key={"pk": item["pk"], "sk": item["sk"]})

        self.client = FlaskClient()
