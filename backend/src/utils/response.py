import json
from src.utils.enum import HttpStatus


class Response:
    def __init__(
        self,
        body: dict,
        status: HttpStatus = HttpStatus.OK,
        headers: dict = None,
    ) -> None:
        self.status = status
        self.body = body
        self.headers = {
            "Content-Type": "application/json",
            **(headers or {}),
        }

    def to_json(self):
        return {
            "statusCode": self.status.value,
            "body": json.dumps(self.body),
            "headers": self.headers,
        }


class ErrorResponse(Response):
    def __init__(
        self,
        error: str,
        status: HttpStatus = HttpStatus.INTERNAL_SERVER_ERROR,
        headers: dict = None,
    ) -> None:
        super().__init__({"error": error}, status, headers)
