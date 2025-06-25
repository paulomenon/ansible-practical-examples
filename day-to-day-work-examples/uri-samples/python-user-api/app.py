# This is a simple Flask application that provides a RESTful API for user management.
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for demonstration purposes
users = {} # Dictionary to store user data

@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    users[username] = {"username": username, "email": email}
    print(f"Received user: {username} ({email})")
    return jsonify(data), 201

@app.route('/api/users/<username>', methods=['GET'])
def get_user(username):
    # In a real application, you would fetch the user from a database
    user = users.get(username)
    if user:
        return jsonify(user), 200
    else:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
