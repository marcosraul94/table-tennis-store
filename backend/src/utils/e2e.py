import json
from typing import Optional
from unittest import TestCase
from src.utils.app import create_app
from src.utils.repository import Repository


class FlaskClient:
    def __init__(self):
        self.__app = create_app()

    def post(self, route: str, body: dict, headers: dict = {}):
        with self.__app.test_client() as client:
            return client.post(
                route, json=json.dumps(body), headers=headers
            ).get_json()

    def get(self, route: str, headers: dict = {}):
        with self.__app.test_client() as client:
            return client.get(route, headers=headers).get_json()


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


class UserE2ETestCase(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.email = "hello@email.com"
        data = self.create_user()
        self.headers = {"Authorization": f'Bearer {data["jwt"]}'}

    def create_user(self, email: Optional[str] = None) -> str:
        credentials = {
            "password": "password",
            "email": email if email else self.email,
        }
        return self.client.post("/sign-up", credentials)["data"]
