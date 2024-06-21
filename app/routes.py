
from flask import Blueprint, request, jsonify, g
from .middleware import validate_api_credentials

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Welcome to the ZKTECO API'

@main.route('/add_user', methods=['POST'])
@validate_api_credentials
def add_user():
    data = request.json
    device_config = g.device_config
    success, message = addUser(device_config['ip'], device_config['port'], data['uid'], data['name'],
                               data['privilege'], data['password'], data['group_id'], data['user_id'], data['fingerprints'])
    return jsonify({'success': success, 'message': message})
