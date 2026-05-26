"""
SECURITY TRAINING EXAMPLE
Non-production educational examples of insecure coding patterns.
"""

import os
import sqlite3
import hashlib
import pickle
import subprocess
import requests

# =====================================================
# 1. HARDCODED SECRET
# =====================================================

API_KEY = "HARDCODED_SECRET_KEY"   # ❌ insecure


# =====================================================
# 2. WEAK PASSWORD HASHING
# =====================================================

def weak_hash(password):
    # ❌ MD5 is not safe for passwords
    return hashlib.md5(password.encode()).hexdigest()


# =====================================================
# 3. SQL INJECTION
# =====================================================

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ vulnerable string formatting
    query = f"SELECT * FROM users WHERE username='{username}'"

    cursor.execute(query)
    return cursor.fetchall()


# =====================================================
# 4. COMMAND INJECTION
# =====================================================

def ping_host(host):
    # ❌ unsafe shell command construction
    os.system(f"ping -c 1 {host}")


# =====================================================
# 5. INSECURE DESERIALIZATION
# =====================================================

def load_data(blob):
    # ❌ unsafe deserialization
    return pickle.loads(blob)


# =====================================================
# 6. PATH TRAVERSAL
# =====================================================

def read_file(filename):
    # ❌ attacker can use ../../../
    with open("uploads/" + filename, "r") as f:
        return f.read()


# =====================================================
# 7. SSRF (SERVER-SIDE REQUEST FORGERY)
# =====================================================

def fetch_url(url):
    # ❌ user controls outbound request
    return requests.get(url).text


# =====================================================
# 8. INFORMATION LEAKAGE
# =====================================================

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        # ❌ leaking internal details
        return str(e)


# =====================================================
# 9. UNSAFE FILE UPLOAD NAME
# =====================================================

def save_upload(filename, data):
    # ❌ filename not sanitized
    path = "uploads/" + filename

    with open(path, "wb") as f:
        f.write(data)


# =====================================================
# 10. DEBUG MODE ENABLED
# =====================================================

DEBUG = True   # ❌ should not be enabled in production


# =====================================================
# 11. BROKEN ACCESS CONTROL
# =====================================================

def get_account(user_id):
    # ❌ no authorization check
    return f"Account data for {user_id}"


# =====================================================
# 12. UNSAFE SUBPROCESS USAGE
# =====================================================

def run_command(user_input):
    # ❌ shell=True risk
    subprocess.run(user_input, shell=True)


# =====================================================
# SAFER ALTERNATIVES (examples)
# =====================================================

# - Use environment variables for secrets
# - Use bcrypt/argon2 for passwords
# - Use parameterized SQL queries
# - Avoid shell=True
# - Validate filenames
# - Restrict outbound requests
# - Disable debug mode in production
# - Add authorization checks