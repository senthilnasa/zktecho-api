from functools import wraps
from flask import request, jsonify, abort

def validate_api_credentials(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        data = request.json if request.method == "POST" else request.args
        api_key = data.get('api_key')
        api_secret = data.get('api_secret')
        device_id = data.get('device_id')  # assuming device ID is passed

        # Load config or use global/configured values
        from .config import config  # Assuming config is a dictionary loaded from env.json or similar
        valid = False
        for key in config['api_keys']:
            if key['api_key'] == api_key and key['api_secret'] == api_secret:
                if device_id in key['devices']:
                    valid = True
                    break

        if not valid:
            return jsonify({'success': False, 'message': 'Invalid API credentials or device access'}), 403

        return func(*args, **kwargs)
    return decorated_function
