from src.utils.repository import Repository
from src.utils.serialization import UserSerialization


class UserRepo(Repository):
    EntitySerializationCls = UserSerialization
