from datetime import datetime
from src.utils.entity import Entity


class User(Entity):
    def __init__(
        self,
        email: str,
        encrypted_password: str,
        id: str = None,
        created_at: datetime = None,
    ):
        super().__init__(email, id, created_at)
        self.encrypted_password = encrypted_password
