"""Unit tests for Flask application"""

import pytest
from app.app import app, calculate

@pytest.fixture
def client():
    """Test client fixture"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    """Test index endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    data = response.get_json()
    assert 'message' in data
    assert 'version' in data

def test_health(client):
    """Test health endpoint"""
    response = client.get('/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_info(client):
    """Test info endpoint"""
    response = client.get('/api/info')
    assert response.status_code == 200
    data = response.get_json()
    assert 'application' in data
    assert 'version' in data

def test_calculate_add():
    """Test addition"""
    result = calculate(5, 3, 'add')
    assert result == 8

def test_calculate_subtract():
    """Test subtraction"""
    result = calculate(10, 4, 'subtract')
    assert result == 6

def test_calculate_multiply():
    """Test multiplication"""
    result = calculate(6, 7, 'multiply')
    assert result == 42

def test_calculate_divide():
    """Test division"""
    result = calculate(20, 4, 'divide')
    assert result == 5

def test_calculate_divide_by_zero():
    """Test division by zero error"""
    with pytest.raises(ValueError):
        calculate(10, 0, 'divide')

def test_calculate_invalid_operation():
    """Test invalid operation"""
    with pytest.raises(ValueError):
        calculate(5, 3, 'invalid')

def test_calculate_endpoint_add(client):
    """Test calculator API endpoint"""
    response = client.get('/api/calculate/add/5/3')
    assert response.status_code == 200
    data = response.get_json()
    assert data['result'] == 8

def test_calculate_endpoint_divide_by_zero(client):
    """Test calculator API error handling"""
    response = client.get('/api/calculate/divide/10/0')
    assert response.status_code == 400
    data = response.get_json()
    assert 'error' in data
