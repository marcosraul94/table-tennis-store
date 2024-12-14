from datetime import datetime, UTC
from src.utils.enum import EntityType


class Entity:
    def __init__(
        self,
        pk: str,
        sk: str,
        entity_type: EntityType,
        created_at: datetime = None,
    ):
        self.pk = pk
        self.sk = sk
        self.entity_type = entity_type
        self.created_at = created_at if created_at else datetime.now(UTC)

    def to_dict(self):
        return {
            key: getattr(self, key)
            for key in dir(self)
            if not key.startswith("_") and not callable(getattr(self, key))
        }
