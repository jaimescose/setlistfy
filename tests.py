from fastapi.testclient import TestClient


client = TestClient(app)


def test_app():
    response = client.get("/")
    data = response.json()
    assert data == {"Hello": "World"}
