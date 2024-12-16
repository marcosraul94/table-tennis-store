import unittest
from src.utils.auth import JWT, Password


class TestJWT(unittest.TestCase):
    def test_create_token_is_different_every_time(self):
        email = "hello@email.com"

        self.assertNotEqual(JWT.create_token(email), JWT.create_token(email))

    def test_validate_email_correctly(self):
        email = "hello@email.com"
        token = JWT.create_token(email)
        extracted_email = JWT.extract_email(token)

        self.assertEqual(extracted_email, email)

    def test_validate_email_incorrectly(self):
        email = "hello@email.com"
        token = f"{JWT.create_token(email)}something else"

        with self.assertRaises(Exception):
            JWT.extract_email(token)


class TestPassword(unittest.TestCase):
    def test_hashing_is_different_every_time(self):
        plain_text_password = "password"

        self.assertNotEqual(
            Password.hash(plain_text_password),
            Password.hash(plain_text_password),
        )

    def test_verifying_correctly(self):
        plain_text_password = "password"
        hashed = Password.hash(plain_text_password)

        self.assertTrue(Password.verify(plain_text_password, hashed))

    def test_verifying_incorrectly(self):
        with self.assertRaises(Exception):
            Password.verify("password", "wrong")


if __name__ == "__main__":
    unittest.main()
