import jwt
import argon2
from flask import request
from typing import Callable
from functools import wraps
from src.utils.date import now
from src.utils.enum import HttpStatus
from src.utils.env import jwt_secret_key
from src.utils.constant import jwt_algorithm
from src.utils.response import ErrorResponse
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
    def __get_hasher():
        return argon2.PasswordHasher(time_cost=1)

    @classmethod
    def hash(cls, plain_text_password: str) -> str:
        return cls.__get_hasher().hash(plain_text_password)

    @classmethod
    def verify(cls, plain_text_password: str, hashed_password: str) -> bool:
        return cls.__get_hasher().verify(
            hashed_password,
            plain_text_password,
        )


def validate_protected_route(func: Callable):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header:
            return ErrorResponse(
                "Missing Authorization header",
                status=HttpStatus.UNAUTHORIZED,
            ).to_json_response()

        scheme = "Bearer "
        if not auth_header.startswith(scheme):
            return ErrorResponse(
                "Invalid Authorization header",
                status=HttpStatus.UNAUTHORIZED,
            ).to_json_response()

        try:
            token = auth_header.split(scheme)[1]

            return func(*args, email=JWT.extract_email(token), **kwargs)

        except Exception:
            return ErrorResponse(
                "Invalid token",
                status=HttpStatus.UNAUTHORIZED,
            ).to_json_response()

    return decorated_function
