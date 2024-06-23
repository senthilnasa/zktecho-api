# ZKTeco API Integration

This repository contains a Flask application designed to interface with ZKTeco devices. It provides a series of API endpoints for managing users and attendance data on ZKTeco devices through network communication.

## Installation

### Cloning the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/senthilnasa/zktecho-api
cd zktecho-api
```

### Running with Docker

Before running the application with Docker, ensure you have Docker installed on your system. Then you can pull the image from Docker Hub and run it:

```bash
docker pull senthilnasa/zktecho-api:latest
docker run -p 5000:5000 $(pwd)/env.json:/app/env.json senthilnasa/zktecho-api
```

In the above command, `$(pwd)/env.json:/app/env.json` specifies the path to your environment configuration file. Make sure to modify your `env.json` based on the `sample.env.json` provided as a reference.

### Environment Configuration

Create `env.json` based on `sample.env.json` provided in the repository to set up necessary API keys, device details, and other configurations:

```json
{
    "api_keys": [
        {
            "api_key": "admin@zktecho-apisenthilnasa.me",
            "api_secret": "1234567890",
            "devices": ["device_id_1", "device_id_2"]
        }
    ],
    "devices": [
        {
            "device_id": "device_id_1",
            "ip": "10.10.3.8",
            "port": 4370,
            "password": "123456"
        },
        {
            "device_id": "device_id_2",
            "ip": "10.10.3.8",
            "port": 4370,
            "password": "123456"
        }
    ]
}

```

## API Endpoints

### General Routes

- `GET /` - Welcome route to confirm the API is operational.

### User Management

- `POST /add_user` - Adds a new user to the specified ZKTeco device.
- `DELETE /delete_user` - Deletes a user from the specified ZKTeco device.

### Attendance Management

- `GET /get_users` - Retrieves a list of all users from the specified ZKTeco device.
- `GET /get_attendance` - Retrieves attendance data from the specified ZKTeco device.
- `DELETE /clear_attendance` - Clears all attendance data from the specified ZKTeco device.

### Biometric Management

- `POST /add_finger` - Enrolls a fingerprint for a user on the specified ZKTeco device.
- `POST /add_face` - Enrolls face data for a user on the specified ZKTeco device.
- `DELETE /delete_finger` - Deletes a fingerprint for a user on the specified ZKTeco device.

## Running the Application

To run the application, use the following commands:

```bash
export FLASK_APP=run.py
flask run
```

This will start the Flask server on `localhost:5000` by default.

## Security

This API uses middleware to validate API keys and device access. Ensure your API keys and device settings are kept secure and are not exposed publicly.

## Contributions

Contributions to this project are welcome. Please fork the repository and submit a pull request with your features or fixes.
