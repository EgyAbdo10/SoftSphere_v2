#!/usr/bin/env/python3


from flask import request, jsonify, abort
from models import storage
from models.users import User
from api.v1.views import app_views

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_all_users():
    """Retrieve all users"""
    users = [user.to_dict() for user in storage.all("User").values()]
    return jsonify(users)

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """Retrieve a specific user by ID"""
    user = storage.find("User", user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user.to_dict())

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """Create a new user"""
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    new_user = User(**data)
    new_user.save()
    return jsonify(new_user.to_dict()), 201

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user by ID"""
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    user = storage.find("User", user_id)
    if not user:
        abort(404, description="User not found")
    for key, value in data.items():
        setattr(user, key, value)
    user.save()
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user by ID"""
    user = storage.find("User", user_id)
    if not user:
        abort(404, description="User not found")
    storage.delete(user)
    return '', 204