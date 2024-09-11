#!/usr/bin/env python3

from flask import request, jsonify, abort, make_response
from models import storage, storage_type
from models.project import Project
from api.v1.views import app_views
from sqlalchemy.exc import DataError, IntegrityError


@app_views.route('/projects', methods=['GET'], strict_slashes=False)
def get_all_projects():
    """
    Retrieve all projects from the database.
    """
    projects = [obj.to_dict() for obj in storage.all("Project").values()]
    return jsonify(projects)

@app_views.route('/projects/<project_id>', methods=['GET'], strict_slashes=False)
def get_project(project_id):
    """
    Retrieve a specific project by its ID.
    """
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")
    return jsonify(project.to_dict())

@app_views.route('/projects', methods=['POST'], strict_slashes=False)
def create_project():
    """
    Create a new project.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    if storage_type == "db":
        if "tools" in data:
            tools = []
            for tool_id in data["tools"]:
                tool_obj = storage.find("Tool", tool_id)
                if tool_obj:
                    tools.append(tool_obj)
            data["tools"] = tools
    new_project = Project(**data)
    error = new_project.save() # return None if no exception raised
    if error:
        return jsonify({"message": error}), 400

    return jsonify(new_project.to_dict()), 201

@app_views.route('/projects/<project_id>', methods=['PUT'], strict_slashes=False)
def update_project(project_id):
    """
    Update an existing project.
    """
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")

    for key, value in data.items():
        setattr(project, key, value)
    error = project.save()
    if error:
        return jsonify({"message": error}), 400

    return jsonify(project.to_dict())

@app_views.route('/projects/<project_id>', methods=['DELETE'], strict_slashes=False)
def delete_project(project_id):
    """
    Delete a specific project by its ID.
    """
    project = storage.find("Project", project_id)
    if not project:
        abort(404, description="Project not found")
    storage.delete(project)
    return '', 204

@app_views.route("/project_search", methods=["POST"], strict_slashes=False)
def filter_projects():
    """filter projects based on category ids and/or tools useed"""
    data = request.get_json()
    if not data:
        abort(400, description="Not a JSON")

    projects_list = []
    if len(data) == 0 or ("categories" not in data and
                          "tools" not in data):
        projects_list = list(storage.all("Project").values())

    categories = data.get("categories", None)
    tools = data.get("tools", None)


    if categories:
        for cat in categories:
            filtered_projects = storage.filter(
                "Project", "category_id", "eq", cat)
            projects_list += filtered_projects

    if tools:
        filtered_list = []

        if not projects_list:
            projects_list = list(storage.all("Project").values())

        for project in projects_list:

            if storage_type == "db":
                project_tools = [
                        project_tool.id for project_tool in project.tools
                        ]

            else:
                project_tools = project.tools

            if all([tool in project_tools for tool in tools]):
                filtered_list.append(project)
        
        projects_list = filtered_list

    projects_list = [project.to_dict() for project in projects_list]

    return jsonify(projects_list)
