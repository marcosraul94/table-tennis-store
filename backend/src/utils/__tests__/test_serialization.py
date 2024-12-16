import unittest
from decimal import Decimal
from datetime import datetime
from src.utils.serialization import (
    DatetimeSerialization,
    DecimalSerialization,
    DictSerialization,
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


if __name__ == "__main__":
    unittest.main()
