#!/usr/bin/env python3
"""
no coomment for now enjoy

"""


from flask import request, jsonify, abort
from models import storage
from models.category import Category
from api.v1.views import app_views

@app_views.route('/categories', methods=['GET'], strict_slashes=False)
def get_all_categories():
    """Retrieve all categories"""
    categories = [category.to_dict() for category in storage.all("Category").values()]
    return jsonify(categories)

@app_views.route('/categories/<category_id>', methods=['GET'], strict_slashes=False)
def get_category(category_id):
    """Retrieve a specific category by ID"""
    category = storage.find("Category", category_id)
    if not category:
        abort(404, description="Category not found")
    return jsonify(category.to_dict())

@app_views.route('/categories', methods=['POST'], strict_slashes=False)
def create_category():
    """Create a new category"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    new_category = Category(**data)
    error = new_category.save()
    if error:
        return jsonify({"message": error}), 400

    return jsonify(new_category.to_dict()), 201

@app_views.route('/categories/<category_id>', methods=['PUT'], strict_slashes=False)
def update_category(category_id):
    """Update a category by ID"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    category = storage.find("Category", category_id)
    if not category:
        abort(404, description="Category not found")
    for key, value in data.items():
        setattr(category, key, value)

    error = category.save()
    if error:
        return jsonify({"message": error}), 400

    return jsonify(category.to_dict())

@app_views.route('/categories/<category_id>', methods=['DELETE'], strict_slashes=False)
def delete_category(category_id):
    """Delete a category by ID"""
    category = storage.find("Category", category_id)
    if not category:
        abort(404, description="Category not found")
    storage.delete(category)
    return '', 204
