import json

def load_config(filename='env.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}
    except json.JSONDecodeError:
        print("Error decoding JSON from config file")
        return {}

config = load_config()