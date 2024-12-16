import uuid
from typing import Optional
from datetime import datetime, UTC


class Entity:
    def __init__(
        self,
        email: str,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.email = email
        self.id = id if id else str(uuid.uuid4())
        self.created_at = created_at if created_at else datetime.now(UTC)

    def to_dict(self) -> dict:
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_") and not callable(getattr(self, key))
        }

    def __eq__(self, value):
        if not isinstance(value, self.__class__):
            return False

        return self.to_dict() == value.to_dict()
