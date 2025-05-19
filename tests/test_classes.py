def test_create_class(client):
    response = client.post("api/v1/classes", json={
        "title": "Test Class",
        "description": "This is a test class",
        "datetime": "2023-08-15T10:00:00",
        "duration_minutes": 60,
        "status": "scheduled",
        "student_id": 1
    })
    assert response.status_code == 200 or response.status_code == 201
    
def test_list_classes(client):
    response = client.get("/classes")
    assert response.status_code == 200