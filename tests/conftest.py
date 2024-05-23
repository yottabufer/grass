import pytest
from starlette.testclient import TestClient

from tasks.main import app


@pytest.fixture(scope='session')
def test_app():
    """
    Создание тестового приложения с фикстурами
    """
    with TestClient(app) as client:
        yield client
