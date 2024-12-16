from enum import Enum


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"


class HttpStatus(Enum):
    OK = 200
    INTERNAL_SERVER_ERROR = 500


class ENV(Enum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class EntityType(Enum):
    USER = "USER"
    PRODUCT = "PRODUCT"
