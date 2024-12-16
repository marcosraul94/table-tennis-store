import unittest
from src.utils.date import now
from src.utils.enum import HttpStatus
from src.utils.e2e import E2ETestCase
from src.views.sign_up import SignUpView


class TestSignUpView(E2ETestCase):
    def test_created_user(self):
        response = SignUpView.post(
            email="hello@email.com",
            password="plain text password",
        )

        user = response.data["user"]

        self.assertEqual(response.status, HttpStatus.OK)
        self.assertEqual(user["email"], "hello@email.com")
        self.assertIsNotNone(user["email"])
        self.assertEqual(
            user["created_at"].date(),
            now().date(),
        )
        self.assertIsNotNone(response.data["jwt"])


if __name__ == "__main__":
    unittest.main()
