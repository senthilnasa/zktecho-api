import os
import json
from dotenv import load_dotenv

load_dotenv()

def get_config():
    config_json = os.getenv('CONFIG_JSON')
    if config_json:
        return json.loads(config_json)
    return {}