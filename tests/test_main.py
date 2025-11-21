from app.main import app

def test_ping():
    for i in range(100):
     client = app.test_client()
     response = client.get("/ping")
     assert response.status_code == 200
     assert response.get_json() == {"message": "pong!"}
