from enum import Enum
from typing import Optional
from decimal import Decimal
from datetime import datetime, date
from src.entities.user import User
from src.utils.entity import Entity


class DatetimeSerialization:
    @classmethod
    def serialize(cls, value: datetime) -> str:
        return value.isoformat()

    @classmethod
    def deserialize(cls, value: str) -> datetime:
        return datetime.fromisoformat(value)


class DateSerialization(DatetimeSerialization):
    @classmethod
    def serialize(cls, value: date) -> str:
        return super().serialize(value)

    @classmethod
    def deserialize(cls, value: str) -> date:
        return super().deserialize(value).date()


class EnumSerialization:
    @classmethod
    def serialize(cls, value: Enum) -> str:
        return value.value

    @classmethod
    def deserialize(cls, value: str, enumCls: Enum) -> Enum:
        return enumCls(value)


class DecimalSerialization:
    @classmethod
    def serialize(cls, value: Decimal) -> str:
        return str(value)

    @classmethod
    def deserialize(cls, value: str) -> Decimal:
        return Decimal(value)


class DictSerialization:
    @classmethod
    def serialize(cls, value: dict) -> dict:
        serialized = {}

        for k, v in value.items():
            if isinstance(v, datetime):
                serialized[k] = DatetimeSerialization.serialize(v)
            elif isinstance(v, Enum):
                serialized[k] = EnumSerialization.serialize(v)
            elif isinstance(v, Decimal):
                serialized[k] = DecimalSerialization.serialize(v)
            elif isinstance(v, dict):
                serialized[k] = DictSerialization.serialize(v)
            else:
                serialized[k] = v

        return serialized


class EntitySerialization:
    EntityCls: Entity = Entity

    @classmethod
    def create_type(cls) -> str:
        return cls.EntityCls.__name__

    @classmethod
    def create_pk(cls, email: str) -> str:
        return f"{cls.create_type()}#{email}"

    @classmethod
    def create_sk(cls, email: str) -> str:
        return cls.create_pk(email)

    @classmethod
    def to_item(
        cls,
        entity: Entity,
        pk: Optional[str] = None,
        sk: Optional[str] = None,
    ) -> dict:
        item = {
            **entity.to_dict(),
            "pk": pk if pk else cls.create_pk(entity.email),
            "sk": sk if sk else cls.create_sk(entity.email),
            "type": cls.create_type(),
        }

        return DictSerialization.serialize(item)

    @classmethod
    def to_entity(
        cls,
        item: dict,
        keys_to_skip=["pk", "sk", "type"],
        other_values={},
    ) -> Entity:
        kwargs = {k: v for k, v in item.items() if k not in keys_to_skip}
        kwargs = {
            **kwargs,
            "created_at": DatetimeSerialization.deserialize(
                kwargs["created_at"]
            ),
            **other_values,
        }

        return cls.EntityCls(**kwargs)


class UserSerialization(EntitySerialization):
    EntityCls = User
