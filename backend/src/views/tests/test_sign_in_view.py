import unittest
from src.utils.enum import HttpStatus
from src.utils.e2e import E2ETestCase


class TestSignUpView(E2ETestCase):
    def setUp(self):
        super().setUp()
        self.credentials = {
            "email": "hello@email.com",
            "password": "plain text password",
        }
        self.client.post("/sign-up", self.credentials)

    def test_login_after_creating_user(self):
        response = self.client.post("/sign-in", self.credentials)

        self.assertEqual(response["status"], HttpStatus.OK.value)
        self.assertIsNotNone(response["data"]["jwt"])

    def test_login_with_invalid_email(self):
        response = self.client.post(
            "/sign-in",
            {**self.credentials, "email": "wrong"},
        )

        self.assertEqual(response["error"], "Invalid email and password")

    def test_login_with_invalid_password(self):
        response = self.client.post(
            "/sign-in",
            {**self.credentials, "password": "wrong"},
        )

        self.assertEqual(response["error"], "Invalid email and password")


if __name__ == "__main__":
    unittest.main()
