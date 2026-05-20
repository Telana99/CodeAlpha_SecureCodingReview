import os
import sqlite3
import hashlib
import subprocess
import json

# Fix 1: No hardcoded credentials — use environment variables
import os
USERNAME = os.environ.get("APP_USERNAME", "admin")
PASSWORD = os.environ.get("APP_PASSWORD", "")
SECRET_KEY = os.environ.get("APP_SECRET_KEY", "")

# Fix 2: Strong password hashing (SHA-256 instead of MD5)
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Fix 3: Parameterized query — prevents SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    return cursor.fetchall()

# Fix 4: No shell=True — prevents Command Injection
def ping_host(host):
    result = subprocess.call(["ping", host], shell=False)
    return result

# Fix 5: Use JSON instead of pickle — prevents Insecure Deserialization
def load_data(filename):
    with open(filename, "r") as f:
        return json.load(f)

# Fix 6: Debug mode off, no hardcoded IPs
DEBUG = False
SERVER_IP = os.environ.get("SERVER_IP", "127.0.0.1")
SERVER_PORT = int(os.environ.get("SERVER_PORT", "8080"))

# Fix 7: No shell=True in subprocess
def run_command(user_input):
    allowed_commands = ["ls", "whoami", "date"]
    if user_input in allowed_commands:
        subprocess.call([user_input], shell=False)
    else:
        print("Command not allowed!")

# Fix 8: Input validation before deleting file
def delete_file(filename):
    if os.path.exists(filename) and filename.endswith(".tmp"):
        os.remove(filename)
    else:
        print("Invalid or unauthorized file deletion attempt!")

print("App started. Debug mode:", DEBUG)