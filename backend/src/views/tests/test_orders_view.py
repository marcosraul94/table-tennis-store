import unittest
from src.utils.enum import HttpStatus
from src.utils.e2e import UserE2ETestCase


class TestGetOrders(UserE2ETestCase):
    def test_get_orders(self):
        response = self.client.get("/orders", self.headers)

        self.assertEqual(response["status"], HttpStatus.OK.value)
        self.assertNotIn("error", response)

    def test_cannot_get_orders_if_not_logged(self):
        response = self.client.get("/orders")

        self.assertEqual(response["error"], "Missing Authorization header")


if __name__ == "__main__":
    unittest.main()
