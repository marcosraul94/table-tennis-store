from src.utils.view import View


class UserView(View):
    route = '/user'

    def get(self) -> dict:
        return {}
