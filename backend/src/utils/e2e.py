from unittest import TestCase
from src.utils.repository import Repository


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
