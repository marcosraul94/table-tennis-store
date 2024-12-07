from typing import Optional
from src.utils.enum import HttpMethod, Stage
from src.utils.env import stage


class ApiGatewayEvent:
    def __init__(self, raw_event) -> None:
        self.__raw_event = raw_event

    @property
    def body(self) -> Optional[dict]:
        return self.__raw_event["body"]

    @property
    def http_method(self) -> HttpMethod:
        return HttpMethod(self.__raw_event["requestContext"]["http"]["method"])

    @property
    def route(self) -> str:
        return self.__raw_event["requestContext"]["http"]["path"]

    @property
    def email(self) -> str:
        if stage == Stage.LOCAL:
            return "test"

        authorizer = self.__raw_event["requestContext"]["authorizer"]
        return authorizer["jwt"]["claims"]["email"]
