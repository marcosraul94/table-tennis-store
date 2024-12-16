import unittest
from decimal import Decimal
from datetime import datetime
from src.utils.entity import Entity
from src.entities.user import User
from src.utils.serialization import (
    DatetimeSerialization,
    DecimalSerialization,
    DictSerialization,
    EntitySerialization,
    UserSerialization,
)


class TestDatetimeSerialization(unittest.TestCase):
    def test_serialize(self):
        date_obj = datetime(year=2024, month=12, day=15)
        expected_date_str = "2024-12-15T00:00:00"

        self.assertEqual(
            DatetimeSerialization.serialize(date_obj),
            expected_date_str,
        )

    def test_deserialize(self):
        date_str = "2024-12-15T00:00:00"
        expected_date_obj = datetime(year=2024, month=12, day=15)

        self.assertEqual(
            DatetimeSerialization.deserialize(date_str),
            expected_date_obj,
        )


class TestDecimalSerialization(unittest.TestCase):
    def test_serialize(self):
        decimal_obj = Decimal("12.14")
        expected_decimal_str = "12.14"

        self.assertEqual(
            DecimalSerialization.serialize(decimal_obj),
            expected_decimal_str,
        )

    def test_deserialize(self):
        decimal_str = "12.14"
        expected_decimal_obj = Decimal("12.14")

        self.assertEqual(
            DecimalSerialization.deserialize(decimal_str),
            expected_decimal_obj,
        )


class TestDictSerialization(unittest.TestCase):
    def test_serialize(self):
        dict_obj = {
            "created_at": datetime(year=2024, month=12, day=15),
            "name": "Sophie",
            "order": {"amount": Decimal("12.14")},
        }
        expected_dict_obj = {
            "created_at": "2024-12-15T00:00:00",
            "name": "Sophie",
            "order": {"amount": "12.14"},
        }

        self.assertDictEqual(
            DictSerialization.serialize(dict_obj),
            expected_dict_obj,
        )


class TestEntitySerialization(unittest.TestCase):
    def test_create_type(self):
        type_str = EntitySerialization.create_type()
        expected_type_str = "Entity"

        self.assertEqual(
            type_str,
            expected_type_str,
        )

    def test_create_pk(self):
        pk_str = EntitySerialization.create_sk("hello@email.com")
        expected_pk_str = "Entity#hello@email.com"

        self.assertEqual(
            pk_str,
            expected_pk_str,
        )

    def test_create_sk(self):
        sk_str = EntitySerialization.create_sk("hello@email.com")
        expected_sk_str = "Entity#hello@email.com"

        self.assertEqual(
            sk_str,
            expected_sk_str,
        )

    def test_to_item(self):
        entity_obj = Entity(
            id="id",
            email="hello@email.com",
            created_at=datetime(year=2024, month=12, day=15),
        )
        expected_item_dict = {
            "pk": "Entity#hello@email.com",
            "sk": "Entity#hello@email.com",
            "type": "Entity",
            "id": "id",
            "email": "hello@email.com",
            "created_at": "2024-12-15T00:00:00",
        }

        self.assertEqual(
            EntitySerialization.to_item(entity_obj),
            expected_item_dict,
        )

    def test_to_entity(self):
        item_dict = {
            "pk": "Entity#hello@email.com",
            "sk": "Entity#hello@email.com",
            "type": "Entity",
            "id": "id",
            "email": "hello@email.com",
            "created_at": "2024-12-15T00:00:00",
        }
        expected_entity_obj = Entity(
            id="id",
            email="hello@email.com",
            created_at=datetime(year=2024, month=12, day=15),
        )

        self.assertEqual(
            EntitySerialization.to_entity(item_dict),
            expected_entity_obj,
        )


class TestUserSerialization(unittest.TestCase):
    def test_to_item(self):
        user_obj = User(
            id="id",
            email="hello@email.com",
            created_at=datetime(year=2024, month=12, day=15),
        )
        expected_item_dict = {
            "pk": "User#hello@email.com",
            "sk": "User#hello@email.com",
            "type": "User",
            "id": "id",
            "email": "hello@email.com",
            "created_at": "2024-12-15T00:00:00",
        }

        self.assertEqual(
            UserSerialization.to_item(user_obj),
            expected_item_dict,
        )

    def test_to_entity(self):
        item_dict = {
            "pk": "User#hello@email.com",
            "sk": "User#hello@email.com",
            "type": "User",
            "id": "id",
            "email": "hello@email.com",
            "created_at": "2024-12-15T00:00:00",
        }
        expected_user_obj = User(
            id="id",
            email="hello@email.com",
            created_at=datetime(year=2024, month=12, day=15),
        )

        self.assertEqual(
            UserSerialization.to_entity(item_dict),
            expected_user_obj,
        )


if __name__ == "__main__":
    unittest.main()
