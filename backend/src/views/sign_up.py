import argon2
from src.utils.jwt import JWT
from src.utils.view import View
from src.entities.user import User
from src.utils.response import Response
from src.repositories.user import UserRepo


class SignUpView(View):
    @staticmethod
    def post(email: str, password: str):
        user = User(
            email,
            encrypted_password=argon2.PasswordHasher().hash(password),
        )
        UserRepo().create([user])

        return Response(
            data={
                "user": user.to_dict(keys_to_remove=["encrypted_password"]),
                "jwt": JWT.create_token(email),
            }
        )
