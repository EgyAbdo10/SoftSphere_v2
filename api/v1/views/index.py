#!/usr/bin/env python3

from flask import jsonify
from api.v1.views import app_views
from models import storage

@app_views.route('/status')
def api_status():
    response = {'status': "OK"}
    return jsonify(response)

@app_views.route('/stats')
def get_stats():
    stats = {
        'projects': storage.count('Project'),
        'users': storage.count('User'),
        'categories': storage.count('Category'),
        'tools': storage.count('Tool')
    }
    return jsonify(stats)
