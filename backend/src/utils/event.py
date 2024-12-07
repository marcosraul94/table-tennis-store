from typing import Optional
from src.utils.enum import HttpMethod, Stage
from src.utils.env import stage


class ApiGatewayEvent:
    def __init__(self, event) -> None:
        self._event = event

    @property
    def body(self) -> Optional[dict]:
        return self._event['body']

    @property
    def http_method(self) -> HttpMethod:
        return HttpMethod(self._event['requestContext']['http']['method'])

    @property
    def email(self) -> str:
        if stage == Stage.LOCAL:
            return 'test'

        authorizer = self._event['requestContext']['authorizer']
        return authorizer['jwt']['claims']['email']
