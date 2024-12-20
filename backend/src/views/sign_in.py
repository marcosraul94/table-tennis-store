from werkzeug.exceptions import Unauthorized
from src.utils.view import View
from src.entities.user import User
from src.utils.response import Response
from src.utils.auth import JWT, Password
from src.repositories.user import UserRepo


class SignInView(View):
    @staticmethod
    def post(email: str, password: str):
        users = UserRepo().query_by_email(email)
        if not users:
            raise Unauthorized("Does not exist user with those credentials")

        user: User = users[0]
        Password.verify(password, user.hashed_password)

        return Response(
            data={
                "user": user.to_dict(keys_to_remove=["hashed_password"]),
                "jwt": JWT.create_token(email),
            }
        )
