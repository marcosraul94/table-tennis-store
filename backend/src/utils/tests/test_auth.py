import unittest
from src.utils.app import create_app
from src.utils.enum import HttpMethod, HttpStatus
from src.utils.auth import JWT, Password, validate_protected_route


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


class TestValidateProtectedRoute(unittest.TestCase):
    def setUp(self):
        self.route = "/protected"
        self.app = create_app()

        @self.app.route(self.route, methods=[HttpMethod.GET.value])
        @validate_protected_route
        def protected_route(email: str):
            return {"email": email}

    def test_protected_route_no_header(self):
        with self.app.test_client() as client:
            response = client.get(self.route)

        self.assertEqual(response.status_code, HttpStatus.UNAUTHORIZED.value)
        self.assertEqual(
            response.get_json(), {"error": "Missing Authorization header"}
        )

    def test_protected_route_invalid_header(self):
        with self.app.test_client() as client:
            response = client.get(
                self.route, headers={"Authorization": "InvalidToken"}
            )

        self.assertEqual(response.status_code, HttpStatus.UNAUTHORIZED.value)
        self.assertEqual(
            response.get_json(), {"error": "Invalid Authorization header"}
        )

    def test_protected_route_invalid_token(self):
        with self.app.test_client() as client:
            response = client.get(
                self.route, headers={"Authorization": "Bearer something"}
            )

        self.assertEqual(response.status_code, HttpStatus.UNAUTHORIZED.value)
        self.assertEqual(response.get_json(), {"error": "Invalid token"})

    def test_protected_route_valid_token(self):
        with self.app.test_client() as client:
            email = "hello@email.com"
            authorization = f"Bearer {JWT.create_token(email)}"

            response = client.get(
                self.route,
                headers={"Authorization": authorization},
            )

        self.assertEqual(response.status_code, HttpStatus.OK.value)
        self.assertEqual(response.get_json(), {"email": email})


if __name__ == "__main__":
    unittest.main()
