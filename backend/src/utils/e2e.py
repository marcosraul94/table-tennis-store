from unittest import TestCase
from src.utils.repository import Repository


class E2ETestCase(TestCase):
    def setUp(self):
        table = Repository().table

        response = table.scan()
        items = response["Items"]

        with table.batch_writer() as batch:
            for item in items:
                batch.delete_item(Key={"pk": item["pk"], "sk": item["sk"]})
