from contracts import User
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root() -> dict:
    """Path entrypoint. Returns \"Hello, World!\" message"""
    return {"message": "Hello, World"}


@router.get("/ai_greeting")
async def ai_doorman(name: str = "World") -> dict:
    """Query entrypoint. Greets users by their name"""
    return {"message": f"Hello {name}! (The message is AI-generated)"}


@router.post("/oldifier/")
async def cool_oldifying_service(user: User) -> list[dict]:
    """Request body entrypoint. Returns comment in message and (optionally) increases user's age"""
    message: str
    if user.age < 0:
        message = "Do not lie! You cannot be so young! Now you'll be 10 years old"
        user.age = 10
    elif 0 <= user.age < 30:
        user.age += 20
        message = "You are oldified!"
    else:
        message = "Oh! You are already so old! It is impolite to oldify you!"
        user.name = "Senior User " + user.name
    return [{"message": message}, user.dict()]
