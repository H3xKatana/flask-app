from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from flask_auth_sys import *
import datetime
import os

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# In-memory database (replace with real DB in production)
users = {}
blacklisted_tokens = set()

# Helper functions
def generate_token(user_id):
    return jwt.encode({
        'sub': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }, os.getenv('SECRET_KEY', 'default-secret-key'), algorithm='HS256')

def validate_token(token):
    try:
        payload = jwt.decode(
            token, 
            os.getenv('SECRET_KEY', 'default-secret-key'),
            algorithms=['HS256']
        )
        return payload
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        return None

# Routes
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({"error": "Missing email or password"}), 400
    
    if data['email'] in users:
        return jsonify({"error": "User already exists"}), 409
    
    users[data['email']] = {
        'password': generate_password_hash(data['password']),
        'id': len(users) + 1
    }
    
    return jsonify({"message": "User created successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    auth = request.get_json()
    
    if not auth or 'email' not in auth or 'password' not in auth:
        return jsonify({"error": "Missing credentials"}), 400
    
    user = users.get(auth['email'])
    if not user or not check_password_hash(user['password'], auth['password']):
        return jsonify({"error": "Invalid credentials"}), 401
    
    token = generate_token(user['id'])
    return jsonify({"token": token}), 200

@auth_bp.route('/validate', methods=['POST'])
def validate():
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    
    if not token or token in blacklisted_tokens:
        return jsonify({"error": "Invalid token"}), 401
    
    payload = validate_token(token)
    if not payload:
        return jsonify({"error": "Invalid token"}), 401
    
    return jsonify({
        "user_id": payload['sub'],
        "expires": payload['exp']
    }), 200

@auth_bp.route('/logout', methods=['POST'])
def logout():
    token = request.headers.get('Authorization', '').split('Bearer ')[-1]
    blacklisted_tokens.add(token)
    return jsonify({"message": "Successfully logged out"}), 200

@auth_bp.route('/reset-password', methods=['POST'])
def reset_password():
    data = request.get_json()
    
    if 'email' not in data:
        return jsonify({"error": "Email required"}), 400
    
    # In real app: Send password reset email
    return jsonify({"message": "Reset instructions sent if email exists"}), 200
