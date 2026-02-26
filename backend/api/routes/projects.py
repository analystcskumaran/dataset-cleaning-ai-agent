from flask import Blueprint, request, jsonify

# Create a blueprint for project management
projects_bp = Blueprint('projects', __name__)

# In-memory storage for projects (could be replaced with a database)
projects = {}

@projects_bp.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects), 200

@projects_bp.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    project_id = len(projects) + 1
    projects[project_id] = data
    return jsonify({'id': project_id, 'project': data}), 201

@projects_bp.route('/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    project = projects.get(project_id)
    if project:
        return jsonify(project), 200
    return jsonify({'error': 'Project not found'}), 404

@projects_bp.route('/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    if project_id in projects:
        projects[project_id].update(data)
        return jsonify({'id': project_id, 'project': projects[project_id]}), 200
    return jsonify({'error': 'Project not found'}), 404

@projects_bp.route('/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    if project_id in projects:
        del projects[project_id]
        return jsonify({'message': 'Project deleted'}), 200
    return jsonify({'error': 'Project not found'}), 404

# Note: You need to register this blueprint in your Flask app
# app.register_blueprint(projects_bp)