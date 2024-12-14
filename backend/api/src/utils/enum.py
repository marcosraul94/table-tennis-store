from enum import Enum


class HttpMethod(Enum):
    GET = "get"
    POST = "post"
    DELETE = "delete"
    PATCH = "patch"
    PUT = "put"


class ENV(Enum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class HttpStatus(Enum):
    OK = 200
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
