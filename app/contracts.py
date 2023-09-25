from pydantic import BaseModel


class User(BaseModel):
    """Simple user model"""

    name: str
    age: int
