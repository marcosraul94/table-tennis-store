import unittest
from src.utils.enum import HttpStatus
from src.utils.e2e import E2ETestCase


class TestSignUpView(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.route = "/sign-in"

    def test_login_after_creating_user(self):
        credentials = {
            "email": "hello@email.com",
            "password": "plain text password",
        }

        self.client.post("/sign-up", credentials)
        response = self.client.post("/sign-in", credentials)

        self.assertEqual(response["status"], HttpStatus.OK.value)
        self.assertIsNotNone(response["jwt"])

    def test_login_with_invalid_email(self):
        credentials = {
            "email": "hello@email.com",
            "password": "plain text password",
        }

        response = self.client.post(self.route, credentials)
        self.assertEqual(response["error"], "Invalid email and password")


if __name__ == "__main__":
    unittest.main()
