from typing import Optional
from datetime import datetime
from src.utils.entity import Entity


class User(Entity):
    def __init__(
        self,
        email: str,
        hashed_password: str,
        id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        super().__init__(email, id, created_at)
        self.hashed_password = hashed_password
