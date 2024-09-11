#!/usr/bin/env/python3


from flask import request, jsonify, abort
from models import storage
from models.users import User
from api.v1.views import app_views
from sqlalchemy.exc import DataError, IntegrityError


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
        abort(400, description="Not a JSON")

    new_user = User(**data)
    error = new_user.save()
    print(new_user.to_dict())
    if error:
        return jsonify({"message": error}), 400
    
    return jsonify(new_user.to_dict()), 201


@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """Update a user by ID"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    user = storage.find("User", user_id)
    if not user:
        abort(404, description="User not found")

    for key, value in data.items():
        setattr(user, key, value)
    error = user.save()
    if error:
        return jsonify({"message": error}), 400
    
    return jsonify(user.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """Delete a user by ID"""
    user = storage.find("User", user_id)
    if not user:
        abort(404, description="User not found")
    storage.delete(user)
    return '', 204

@app_views.route("/users/<username>/projects", methods=["GET"], strict_slashes=False)
def user_projects(username):
    """show all projects of a certain user"""
    try:
        user = storage.filter("User", "username", "eq", username)[0]
        projects = [project.to_dict() for project in user.projects]
        return jsonify(projects)
    except Exception as e:
        return jsonify({"message": "Not Found"}), 404
