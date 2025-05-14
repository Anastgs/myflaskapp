# tests/test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_events_endpoint(client):
    response = client.get('/api/events')
    assert response.status_code == 200
    assert 'events' in response.json

def test_news_endpoint(client):
    response = client.get('/api/news')
    assert response.status_code == 200
    assert 'news' in response.json