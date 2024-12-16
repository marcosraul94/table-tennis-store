from src.utils.auth import JWT, Password
from src.utils.view import View
from src.entities.user import User
from src.utils.response import Response
from src.repositories.user import UserRepo


class SignUpView(View):
    @staticmethod
    def post(email: str, password: str):
        user = User(
            email,
            hashed_password=Password.hash(password),
        )
        UserRepo().create([user])

        return Response(
            data={
                "user": user.to_dict(keys_to_remove=["hashed_password"]),
                "jwt": JWT.create_token(email),
            }
        )
