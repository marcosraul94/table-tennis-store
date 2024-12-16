from enum import Enum


class HttpMethod(Enum):
    GET = "GET"
    POST = "POST"
    DELETE = "DELETE"
    PATCH = "PATCH"
    PUT = "PUT"


class ENV(Enum):
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class EntityType(Enum):
    USER = "USER"
    PRODUCT = "PRODUCT"
