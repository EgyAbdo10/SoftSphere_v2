#!/usr/bin/env python3

from flask import request, jsonify, abort
from models import storage
from models.project import Project
from api.v1.views import app_views

@app_views.route('/projects', methods=['GET'], strict_slashes=False)
def get_all_projects():
    """
    Retrieve all projects from the database.
    """
    projects = [obj.to_dict() for obj in storage.all("Project").values()]
    return jsonify(projects)

@app_views.route('/project/<project_id>', methods=['GET'], strict_slashes=False)
def get_project(project_id):
    """
    Retrieve a specific project by its ID.
    """
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")
    return jsonify(project.to_dict())

@app_views.route('/project', methods=['POST'], strict_slashes=False)
def create_project():
    """
    Create a new project.
    """
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    new_project = Project(**data)
    new_project.save()
    return jsonify(new_project.to_dict()), 201

@app_views.route('/project/<project_id>', methods=['PUT'], strict_slashes=False)
def update_project(project_id):
    """
    Update an existing project.
    """
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")
    for key, value in data.items():
        setattr(project, key, value)
    project.save()
    return jsonify(project.to_dict())

@app_views.route('/project/<project_id>', methods=['DELETE'], strict_slashes=False)
def delete_project(project_id):
    """
    Delete a specific project by its ID.
    """
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")
    storage.delete(project)
    return '', 204