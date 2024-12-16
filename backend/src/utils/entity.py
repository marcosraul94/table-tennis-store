from typing import Optional
from datetime import datetime, UTC


class Entity:
    def __init__(
        self, id: str, email: str, created_at: Optional[datetime] = None
    ):
        self.id = id
        self.email = email
        self.created_at = created_at if created_at else datetime.now(UTC)

    def to_dict(self) -> dict:
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_") and not callable(getattr(self, key))
        }
