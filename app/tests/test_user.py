from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_all_user_endpoint():
    response = client.get("/users/get-all-user")
    assert "content-type" in response.headers
    assert response.status_code == 200
    assert response.json() == {"all": "All users"}


def test_get_user_endpoint():
    response = client.get("/users/get-user/20")
    assert response.status_code == 200
    assert response.json() == {"user": f"user Details with the id: 20"}


def test_filter_user_endpoint():
    response = client.get("/users/filter-user/?user_first_name=saviour")
    assert response.status_code == 200
    assert response.json() == {"user": f"list of users with the name: saviour"}


def test_add_user_endpoint():
    response = client.post("/users/add-user", json={"name":"Saviour", "age":1000})
    assert response.status_code == 200
    assert response.json() == {"name":"Saviour", "age":1000}
