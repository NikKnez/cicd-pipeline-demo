#!/usr/bin/env python3
"""
Sample Flask application for CI/CD demo
"""

from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

VERSION = os.getenv('APP_VERSION', '1.0.0')
ENVIRONMENT = os.getenv('FLASK_ENV', 'development')

@app.route('/')
def index():
    """Root endpoint"""
    return jsonify({
        'message': 'CI/CD Pipeline Demo',
        'version': VERSION,
        'environment': ENVIRONMENT
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'version': VERSION,
        'environment': ENVIRONMENT,
        'timestamp': datetime.utcnow().isoformat()
    }), 200

@app.route('/api/info')
def info():
    """Application information"""
    return jsonify({
        'application': 'CI/CD Demo',
        'version': VERSION,
        'environment': ENVIRONMENT,
        'python_version': os.sys.version,
        'timestamp': datetime.utcnow().isoformat()
    })

@app.route('/api/metrics')
def metrics():
    """Basic metrics endpoint"""
    return jsonify({
        'requests': 100,
        'errors': 0,
        'uptime': '24h',
        'version': VERSION
    })

def calculate(a, b, operation='add'):
    """Helper function for testing"""
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    else:
        raise ValueError(f"Unknown operation: {operation}")

@app.route('/api/calculate/<operation>/<int:a>/<int:b>')
def calculate_endpoint(operation, a, b):
    """Calculator endpoint for testing"""
    try:
        result = calculate(a, b, operation)
        return jsonify({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=(ENVIRONMENT == 'development'))
