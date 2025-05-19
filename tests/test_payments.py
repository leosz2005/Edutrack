def test_create_payment(client):
    response = client.post("/api/v1/payments", json={      
        "amount": 0,
        "created_at": "2025-05-18T10:19:19.065Z",
        "student_id": 0,
        "status": "pending"
    })
    assert response.status_code in (200, 201)
    
def test_list_payments(client):
    response = client.get("/api/v1/payments")
    assert response.status_code == 200

    