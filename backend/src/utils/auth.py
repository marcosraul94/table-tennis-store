import jwt
import argon2
from src.utils.date import now
from src.utils.env import jwt_secret_key
from src.utils.constant import jwt_algorithm
from src.utils.serialization import DatetimeSerialization


class JWT:
    @staticmethod
    def create_token(email: str) -> str:
        payload = {
            "email": email,
            "created_at": DatetimeSerialization.serialize(now()),
        }

        return jwt.encode(
            payload,
            key=jwt_secret_key,
            algorithm=jwt_algorithm,
        )

    @staticmethod
    def extract_email(token: str) -> str:
        claims = jwt.decode(token, jwt_secret_key, algorithms=[jwt_algorithm])

        return claims["email"]


class Password:
    @staticmethod
    def hash(plain_text_password: str) -> str:
        return argon2.PasswordHasher().hash(plain_text_password)

    @staticmethod
    def verify(plain_text_password: str, hashed_password: str) -> None:
        argon2.PasswordHasher().verify(hashed_password, plain_text_password)
