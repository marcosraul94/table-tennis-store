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
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Methods": "GET,POST,DELETE,PATCH",
            ** (headers or {}),
        }

    def to_dict(self) -> dict:
        return {
            "statusCode": self.status.value,
            "body": self.body,
            "headers": self.headers,
        }

    def serialize(self) -> dict:
        return {
            **self.to_dict(),
            "body": json.dumps(self.body),
        }


class ErrorResponse(Response):
    def __init__(
        self,
        error: Exception,
        status: HttpStatus = HttpStatus.INTERNAL_SERVER_ERROR,
        headers: dict = None,
    ) -> None:
        super().__init__({"error": error}, status, headers)
