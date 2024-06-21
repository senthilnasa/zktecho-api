from flask import Blueprint, jsonify
main = Blueprint('main', __name__)

from flask import Blueprint, request, jsonify
from .zk_helpers import addUser, addFingerprintFromReader, getAttendance, getUsers, deleteUser, deleteFingerprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Welcome to the ZKTECO API'


@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    success, message = addUser(data['ip'], data['port'], data['uid'], data['name'], data['privilege'],
                               data['password'], data['group_id'], data['user_id'], data['fingerprints'])
    return jsonify({'success': success, 'message': message})

@main.route('/add_fingerprint', methods=['POST'])
def add_fingerprint():
    data = request.json
    success, message = addFingerprintFromReader(data['ip'], data['port'], data['password'], data['uid'], 
                                                data['fid'], data['valid'], data['template'])
    return jsonify({'success': success, 'message': message})

@main.route('/get_attendance', methods=['GET'])
def get_attendance():
    ip = request.args.get('ip')
    port = request.args.get('port')
    password = request.args.get('password')
    success, attendance = getAttendance(ip, port, password)
    return jsonify({'success': success, 'attendance': attendance})

@main.route('/get_users', methods=['GET'])
def get_users():
    ip = request.args.get('ip')
    port = request.args.get('port')
    password = request.args.get('password')
    success, users = getUsers(ip, port, password)
    return jsonify({'success': success, 'users': users})

@main.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.json
    success, message = deleteUser(data['ip'], data['port'], data['password'], data['uid'])
    return jsonify({'success': success, 'message': message})

@main.route('/delete_fingerprint', methods=['POST'])
def delete_fingerprint():
    data = request.json
    success, message = deleteFingerprint(data['ip'], data['port'], data['password'], data['uid'], data['fid'])
    return jsonify({'success': success, 'message': message})

# Ensure to register this blueprint in your app/__init__.py file
