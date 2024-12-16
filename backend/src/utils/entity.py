import uuid
from typing import Optional
from datetime import datetime
from src.utils.date import now


class Entity:
    def __init__(
        self,
        email: str,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.email = email
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else now()

    def to_dict(self, keys_to_remove=[]) -> dict:
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_")
            and not callable(getattr(self, key))
            and key not in keys_to_remove
        }

    def __eq__(self, value):
        if not isinstance(value, self.__class__):
            return False

        return self.to_dict() == value.to_dict()
