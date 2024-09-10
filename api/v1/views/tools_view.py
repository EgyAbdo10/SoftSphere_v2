#!/usr/bin/env python3


from flask import request, jsonify, abort
from models import storage
from models.tools import Tool
from api.v1.views import app_views

@app_views.route('/tools', methods=['GET'], strict_slashes=False)
def get_all_tools():
    """Retrieve all tools"""
    tools = [tool.to_dict() for tool in storage.all("Tool").values()]
    return jsonify(tools)

@app_views.route('/tools/<tool_id>', methods=['GET'], strict_slashes=False)
def get_tool(tool_id):
    """Retrieve a specific tool by ID"""
    tool = storage.find("Tool", tool_id)
    if not tool:
        abort(404, description="Tool not found")
    return jsonify(tool.to_dict())

@app_views.route('/tools', methods=['POST'], strict_slashes=False)
def create_tool():
    """Create a new tool"""
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    new_tool = Tool(**data)
    new_tool.save()
    return jsonify(new_tool.to_dict()), 201

@app_views.route('/tools/<tool_id>', methods=['PUT'], strict_slashes=False)
def update_tool(tool_id):
    """Update a tool by ID"""
    data = request.get_json()
    if not data:
        abort(400, description="No input data provided")
    tool = storage.find("Tool", tool_id)
    if not tool:
        abort(404, description="Tool not found")
    for key, value in data.items():
        setattr(tool, key, value)
    tool.save()
    return jsonify(tool.to_dict())

@app_views.route('/tools/<tool_id>', methods=['DELETE'], strict_slashes=False)
def delete_tool(tool_id):
    """Delete a tool by ID"""
    tool = storage.find("Tool", tool_id)
    if not tool:
        abort(404, description="Tool not found")
    storage.delete(tool)
    return '', 204