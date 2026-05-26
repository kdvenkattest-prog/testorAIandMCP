"""
Educational example: common Python security mistakes
DO NOT USE IN PRODUCTION
"""

import sqlite3
import hashlib
import os

# -----------------------------
# BAD PRACTICE #1: Hardcoded secret
# -----------------------------
API_KEY = "12345-SECRET-KEY"   # ❌ Never hardcode secrets


# Better:
# API_KEY = os.getenv("API_KEY")


# -----------------------------
# BAD PRACTICE #2: Weak password hashing
# -----------------------------
def hash_password(password):
    # ❌ MD5 is insecure for passwords
    return hashlib.md5(password.encode()).hexdigest()


# Better:
# Use bcrypt, argon2, or scrypt


# -----------------------------
# BAD PRACTICE #3: SQL Injection
# -----------------------------
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # ❌ Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)
    return cursor.fetchall()


# Better:
# cursor.execute(
#     "SELECT * FROM users WHERE username = ?",
#     (username,)
# )


# -----------------------------
# BAD PRACTICE #4: Debug info leakage
# -----------------------------
def divide(a, b):
    try:
        return a / b
    except Exception as e:
        # ❌ Reveals internal details
        print("Internal Error:", e)


# Better:
# Log securely without exposing internals


# -----------------------------
# BAD PRACTICE #5: Unsafe shell execution
# -----------------------------
def ping(host):
    # ❌ Command injection risk
    os.system(f"ping -c 1 {host}")


# Better:
# subprocess.run([...], shell=False)