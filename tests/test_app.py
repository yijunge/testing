import pytest
from app import app
import json

@pytest.fixture
def client():
    # Create a test client for the Flask app
    with app.test_client() as client:
        yield client

def test_root(client):
    """Test the root endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {"message": "Hello World"}

def test_create_item(client):
    """Test creating an item"""
    response = client.post('/items', json={"name": "item1"})
    assert response.status_code == 200
    data = response.json
    assert "item_id" in data
    assert data["name"] == "item1"
    assert data["status"] == "created"

def test_read_item(client):
    """Test reading an existing item"""
    # First, create an item
    response = client.post('/items', json={"name": "item2"})
    item_id = response.json["item_id"]

    # Now, read the created item
    response = client.get(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json["item_id"] == item_id
    assert response.json["name"] == "item2"

def test_read_item_not_found(client):
    """Test reading an item that doesn't exist"""
    response = client.get('/items/999')
    assert response.status_code == 404
    assert response.json == {"detail": "Item not found"}

def test_update_item(client):
    """Test updating an existing item"""
    # First, create an item
    response = client.post('/items', json={"name": "item3"})
    item_id = response.json["item_id"]

    # Now, update the item
    response = client.put(f'/items/{item_id}', json={"name": "item3-updated"})
    assert response.status_code == 200
    assert response.json["item_id"] == item_id
    assert response.json["name"] == "item3-updated"
    assert response.json["status"] == "updated"

def test_update_item_not_found(client):
    """Test updating an item that doesn't exist"""
    response = client.put('/items/999', json={"name": "nonexistent"})
    assert response.status_code == 404
    assert response.json == {"detail": "Item not found"}

def test_delete_item(client):
    """Test deleting an existing item"""
    # First, create an item
    response = client.post('/items', json={"name": "item4"})
    item_id = response.json["item_id"]

    # Now, delete the item
    response = client.delete(f'/items/{item_id}')
    assert response.status_code == 200
    assert response.json["item_id"] == item_id
    assert response.json["status"] == "deleted"

def test_delete_item_not_found(client):
    """Test deleting an item that doesn't exist"""
    response = client.delete('/items/999')
    assert response.status_code == 404
    assert response.json == {"detail": "Item not found"}

def test_metrics(client):
    """Test the /metrics endpoint"""
    response = client.get('/metrics')
    assert response.status_code == 200
    assert "http_request_total" in response.data.decode()  # Ensure the metric exists
    assert "http_request_duration_seconds" in response.data.decode()  # Ensure the metric exists

