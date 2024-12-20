from src.utils.view import View
from src.utils.response import Response


class OrdersView(View):
    @staticmethod
    def get(email: str) -> Response:
        return Response(data={"orders": []})
