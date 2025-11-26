import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def reset_rate_limiter():
    # Limpa todas as chaves do MemoryStorage
    storage = app.state.limiter._storage.storage
    if hasattr(storage, "clear"):
        storage.clear()
    yield
