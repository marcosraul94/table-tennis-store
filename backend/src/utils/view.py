from src.utils.event import ApiGatewayEvent


class View:
    route = ''

    def __init__(self, event: ApiGatewayEvent) -> None:
        self.event = event

    def get(self) -> dict:
        raise NotImplementedError

    def post(self) -> dict:
        raise NotImplementedError

    def delete(self) -> dict:
        raise NotImplementedError

    def patch(self) -> dict:
        raise NotImplementedError
