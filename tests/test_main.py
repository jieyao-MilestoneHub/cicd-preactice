from fastapi.testclient import TestClient
from app.main import app
from configs.setting import test_text

client = TestClient(app)

def test_read_root():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": test_text}
