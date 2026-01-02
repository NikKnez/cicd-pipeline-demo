"""Integration tests for API endpoints"""

import pytest
from app.app import app

@pytest.fixture
def client():
    """Test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_full_api_flow(client):
    """Test complete API workflow"""
    # Check health
    response = client.get('/health')
    assert response.status_code == 200
    
    # Get info
    response = client.get('/api/info')
    assert response.status_code == 200
    
    # Test calculation
    response = client.get('/api/calculate/multiply/6/7')
    assert response.status_code == 200
    assert response.get_json()['result'] == 42

def test_metrics_endpoint(client):
    """Test metrics endpoint"""
    response = client.get('/api/metrics')
    assert response.status_code == 200
    data = response.get_json()
    assert 'requests' in data
    assert 'version' in data
