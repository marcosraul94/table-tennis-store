from typing import Optional
from src.utils.enum import HttpMethod, ENV
from src.utils.env import env


class ApiGatewayEvent:
    def __init__(self, raw_event) -> None:
        self.__raw_event = raw_event

    @property
    def body(self) -> Optional[dict]:
        return self.__raw_event["body"]

    @property
    def http_method(self) -> HttpMethod:
        return HttpMethod(self.__raw_event["httpMethod"].lower())

    @property
    def headers(self) -> dict:
        return self.__raw_event["headers"]

    @property
    def route(self) -> str:
        return self.__raw_event["pathParameters"]["proxy"]

    @property
    def email(self) -> str:
        if env == ENV.LOCAL:
            return "test"

        authorizer = self.__raw_event["requestContext"]["authorizer"]
        return authorizer["jwt"]["claims"]["email"]
