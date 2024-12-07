from enum import Enum


class HttpMethod(Enum):
    GET = 'get'
    POST = 'post'
    DELETE = 'delete'
    PATCH = 'patch'


class Stage(Enum):
    LOCAL = 'local'
    CLOUD = 'cloud'
