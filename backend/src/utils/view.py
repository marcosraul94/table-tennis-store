from src.utils.response import Response


class View:
    @staticmethod
    def get() -> Response:
        raise NotImplementedError

    @staticmethod
    def post() -> Response:
        raise NotImplementedError

    @staticmethod
    def delete() -> Response:
        raise NotImplementedError

    @staticmethod
    def patch() -> Response:
        raise NotImplementedError
