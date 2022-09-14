from fastapi import FastAPI
from starlette.testclient import TestClient
import pytest


@pytest.fixture
def app() -> FastAPI:
    from app.api.server import get_application
    app = get_application()
    with TestClient(app) as test_client:  # updated
        # testing
        yield test_client
