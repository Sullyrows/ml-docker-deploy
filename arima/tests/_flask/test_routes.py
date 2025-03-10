import pytest 
import json 

def test_health(client): 
    """test health check endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json == {
        "status": "ok",
        "message": "Service is running"
    }