{% if cookiecutter.database == "Tortoise" -%}
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

from app.core.config import settings


TORTOISE_ORM = {
    "connections": {"default": settings.DATABASE_URI},
    "apps": {
        "models": {
            "models": ["app.users.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}


def register_db(app: FastAPI) -> None:
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=False,
        add_exception_handlers=True,
    )
{% endif -%}
{% if cookiecutter.database == "Beanie" -%}
import motor.motor_asyncio
from beanie import init_beanie

from app.core.config import settings


async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(settings.DATABASE_URI)
    await init_beanie(
        database=client.db_name, document_models=["app.users.models.User"]
    )
{% endif -%}