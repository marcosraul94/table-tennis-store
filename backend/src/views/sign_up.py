from werkzeug.exceptions import Unauthorized
from src.utils.auth import JWT, Password
from src.utils.view import View
from src.entities.user import User
from src.utils.response import Response
from src.repositories.user import UserRepo


class SignUpView(View):
    @staticmethod
    def post(email: str, password: str):
        usersRepo = UserRepo()

        users_with_same_email = usersRepo.query_by_email(email)
        if users_with_same_email:
            raise Unauthorized("Invalid email and password")

        user = User(email, Password.hash(password))
        usersRepo.create([user])

        return Response(
            data={
                "user": user.to_dict(keys_to_remove=["hashed_password"]),
                "jwt": JWT.create_token(email),
            }
        )
