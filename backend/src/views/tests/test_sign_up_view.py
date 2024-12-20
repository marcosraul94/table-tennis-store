import unittest
from datetime import datetime
from src.utils.date import now
from src.utils.enum import HttpStatus
from src.utils.e2e import E2ETestCase


class TestSignUpView(E2ETestCase):
    def test_created_user(self):
        response = self.client.post(
            "/sign-up",
            {
                "email": "hello@email.com",
                "password": "plain text password",
            },
        )

        self.assertEqual(response["status"], HttpStatus.OK.value)

        user = response["data"]["user"]
        self.assertEqual(user["email"], "hello@email.com")
        self.assertIsNotNone(user["email"])
        self.assertEqual(
            datetime.fromisoformat(user["created_at"]).date(),
            now().date(),
        )
        self.assertIsNotNone(response["data"]["jwt"])

    def test_create_same_user(self):
        credentials = {
            "email": "hello@email.com",
            "password": "plain text password",
        }

        response = self.client.post("/sign-up", credentials)
        self.assertNotIn("error", response)

        response = self.client.post("/sign-up", credentials)
        self.assertEqual(response["error"], "Invalid email and password")


if __name__ == "__main__":
    unittest.main()
