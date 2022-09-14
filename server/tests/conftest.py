from fastapi import FastAPI
from httpx import AsyncClient
from asgi_lifespan import LifespanManager
import pytest


@pytest.fixture
def app() -> FastAPI:
    from app.api.server import get_application
    return get_application()


@pytest.fixture
async def client(app: FastAPI) -> AsyncClient:
    async with LifespanManager(app):
        async with AsyncClient(
            app=app,
            base_url="http://testserver",
            headers={"Content-Type": "application/json"}
        ) as client:
            yield client
