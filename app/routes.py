from flask import Blueprint, request, jsonify, g
from .middleware import validate_api_credentials
from .zkteco import getUsers, addUser, getAttendance, clearAttendance, deleteUser, enrollFingerprintFromReader,enrollFaceFromReader

# Initialize the Flask Blueprint
main = Blueprint('main', __name__)

# Index route to check if the API is operational
@main.route('/')
def index():
    return 'Welcome to the ZKTECO API'

# Route to get a list of users from a ZKTeco device
@main.route('/get_users', methods=['GET'])
@validate_api_credentials  # Middleware to validate API credentials before processing the request
def get_users():
    device_config = g.device_config  # Retrieve device configuration stored in the global context
    success,users = getUsers(device_config['ip'], device_config['port'], device_config['password'])
    if not success:
        return jsonify({'success': False, 'message': users})
    return jsonify({'success': True, 'users': users})

# Route to get attendance data from a ZKTeco device
@main.route('/get_attendance', methods=['GET'])
@validate_api_credentials
def get_attendance():
    device_config = g.device_config
    success, attendance = getAttendance(device_config['ip'], device_config['port'], device_config['password'])
    if not success:
        return jsonify({'success': False, 'message': attendance})
    return jsonify({'success': True, 'attendance': attendance})

# Route to clear attendance data on a ZKTeco device
@main.route('/clear_attendance', methods=['DELETE'])
@validate_api_credentials
def clear_attendance():
    device_config = g.device_config
    success, message = clearAttendance(device_config['ip'], device_config['port'], device_config['password'])
    return jsonify({'success': success, 'message': message})

# Route to add a new user to a ZKTeco device
@main.route('/add_user', methods=['POST'])
@validate_api_credentials
def add_user():
    data = request.form
    device_config = g.device_config
    success, message = addUser(device_config['ip'], device_config['port'], device_config['password'], data.get('uid'), data.get('name'),data.get('password'),
                                 data.get('privilege'), data.get('group_id'), data.get('user_id'))
    return jsonify({'success': success, 'message': message})

# Route to enroll a fingerprint to a user on a ZKTeco device
@main.route('/add_finger', methods=['POST'])
@validate_api_credentials
def add_finger():
    data = request.form
    device_config = g.device_config
    success, message = enrollFingerprintFromReader(device_config['ip'], device_config['port'], device_config['password'],data.get('uid'), data.get('temp_id'))
    if not success:
        return jsonify({'success': False, 'message': message})
    else:
        return jsonify({'success': True, 'message': message})

# Route to enroll face data to a user on a ZKTeco device
@main.route('/add_face', methods=['POST'])
@validate_api_credentials
def add_face():
    data = request.form
    device_config = g.device_config
    success, message = enrollFaceFromReader(device_config['ip'], device_config['port'],device_config['password'], data.get('uid'))
    return jsonify({'success': success, 'message': message})

# Route to delete a fingerprint from a user on a ZKTeco device
@main.route('/delete_finger', methods=['DELETE'])
@validate_api_credentials
def delete_finger():
    data = request.form
    device_config = g.device_config
    success, message = addUser(device_config['ip'], device_config['port'], data['uid'], data['name'],
                               data['privilege'], data['password'], data['group_id'], data['user_id'], data['fingerprints'])
    return jsonify({'success': success, 'message': message})

# Route to delete a user from a ZKTeco device
@main.route('/delete_user', methods=['DELETE'])
@validate_api_credentials
def delete_user():
    data = request.form
    device_config = g.device_config
    success, message = deleteUser(device_config['ip'], device_config['port'], data['uid'])
    return jsonify({'success': success, 'message': message})
