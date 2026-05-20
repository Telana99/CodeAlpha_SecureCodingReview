import os
import sqlite3
import hashlib
import subprocess
import pickle

# Vulnerability 1: Hardcoded credentials
USERNAME = "admin"
PASSWORD = "password123"
SECRET_KEY = "mysecretkey12345"

# Vulnerability 2: Weak password hashing (MD5)
def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

# Vulnerability 3: SQL Injection
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# Vulnerability 4: Command Injection
def ping_host(host):
    result = os.system("ping " + host)
    return result

# Vulnerability 5: Insecure Deserialization
def load_data(filename):
    with open(filename, "rb") as f:
        return pickle.load(f)

# Vulnerability 6: Hardcoded IP + debug mode
DEBUG = True
SERVER_IP = "192.168.1.100"
SERVER_PORT = 8080

# Vulnerability 7: Subprocess shell injection
def run_command(user_input):
    subprocess.call(user_input, shell=True)

# Vulnerability 8: No input validation
def delete_file(filename):
    os.remove(filename)

print("App started in DEBUG mode:", DEBUG)
print("Connecting to:", SERVER_IP)