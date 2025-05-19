def test_add_student(client):
    response = client.post("/api/v1/students", json={
        "full_name": "string",
        "email": "user@example.com",
        "phone": "string",
        "birthdate": "2025-05-19",
        "notes": "string"

    })
    assert response.status_code == 200 or response.status_code == 201
