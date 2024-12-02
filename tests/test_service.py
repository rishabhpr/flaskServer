import pytest
from app import create_app
from app.service import PlayerService

@pytest.fixture
def app():
    app = create_app('data/Players.csv')
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_all_players(client):
    response = client.get('/api/players')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) > 0
    assert 'playerID' in data[0]

def test_get_player_by_id(client):
    response = client.get('/api/players/aardsda01')
    assert response.status_code == 200
    player = response.get_json()
    assert player['playerID'] == 'aardsda01'
    assert player['nameFirst'] == 'David'
    assert player['nameLast'] == 'Aardsma'

def test_player_not_found(client):
    response = client.get('/api/players/nonexistent')
    assert response.status_code == 404