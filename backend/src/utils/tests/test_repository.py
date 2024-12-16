import unittest
from src.utils.e2e import E2ETestCase
from src.utils.repository import Repository
from src.utils.entity import Entity
from src.utils.serialization import EntitySerialization


class TestRepository(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.repo = Repository()

    def test_create_returns_items(self):
        entity = Entity(email="hello@email.com")
        expected_items = [EntitySerialization.to_item(entity)]

        self.assertEqual(self.repo.create([entity]), expected_items)

    def test_create_and_query(self):
        email = "hello@email.com"
        expected_entities = [Entity(email)]

        self.repo.create(expected_entities)
        entities = self.repo.query_by_email(email)

        self.assertEqual(entities, expected_entities)


if __name__ == "__main__":
    unittest.main()
