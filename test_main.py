from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Retail Inventory API"}

def test_get_inventory():
    response = client.get("/inventory/toys")
    assert response.status_code == 200
    assert response.json() == {"category": "toys", "stock": 150}
