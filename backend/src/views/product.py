from src.utils.view import View


class ProductView(View):
    route = "product"

    def get(self) -> dict:
        return {"hello": "my darling"}
