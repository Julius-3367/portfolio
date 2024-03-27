#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from flask_mysqldb import MySQL
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Betty'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'guestguru'

mysql = MySQL(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# User Model
class User(UserMixin):
    def __init__(self, id, role):
        self.id = id
        self.role = role

# Load user from database
@login_manager.user_loader
def load_user(user_id):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        return User(user_data['id'], user_data['role'])
    return None

# Create a users table
with app.app_context():
    cursor = mysql.connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(100) NOT NULL,
            role ENUM('admin', 'receptionist') NOT NULL
        )
    """)
    mysql.connection.commit()
    cursor.close()

# Login Route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user_data = cursor.fetchone()
    cursor.close()
    if user_data:
        user = User(user_data['id'], user_data['role'])
        login_user(user)
        return jsonify({"message": "Login successful"})
    return jsonify({"message": "Invalid credentials"}), 401

# Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"})

# Protected Route Example
@app.route('/api/example', methods=['GET'])
@login_required
def protected_example():
    if current_user.role == 'admin':
        return jsonify({"message": "Admin access granted"})
    return jsonify({"message": "You do not have permission to access this resource"}), 403

# User Registration Route
@app.route('/register', methods=['POST'])
def register_user():
    # Implement user registration logic here
    return jsonify({"message": "User registration endpoint"})

# User Management Routes
@app.route('/users', methods=['GET'])
def get_users():
    # Implement logic to get all users
    return jsonify({"message": "Get all users endpoint"})

@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    # Implement logic to update a user
    return jsonify({"message": f"Update user with ID {user_id}"})

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    # Implement logic to delete a user
    return jsonify({"message": f"Delete user with ID {user_id}"})

# Render index.html template
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

