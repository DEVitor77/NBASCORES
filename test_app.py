# Adcionando Testes

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_games(client):
    response = client.get('/games')
    assert response.status_code == 200
    assert len(response.get_json()) == 3
