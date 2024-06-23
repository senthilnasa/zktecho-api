
from functools import wraps
from flask import request, jsonify, abort, g
import json

def load_config():
    with open('env.json', 'r') as file:
        return json.load(file)

config = load_config()

def validate_api_credentials(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        api_key = request.args.get('api_key') or request.form.get('api_key')
        api_secret = request.args.get('api_secret') or request.form.get('api_secret')
        device_id = request.args.get('device_id') or request.form.get('device_id')

        valid = False
        device_config = None

        for key in config['api_keys']:
            if key['api_key'] == api_key and key['api_secret'] == api_secret:
                if device_id in key['devices']:
                    device_config = next((dev for dev in config['devices'] if dev['device_id'] == device_id), None)
                    if device_config:
                        valid = True
                        break

        if not valid or not device_config:
            return jsonify({'success': False, 'message': 'Invalid API credentials or device access'}), 403

        g.device_config = device_config
        return func(*args, **kwargs)
    return decorated_function
