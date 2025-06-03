"""
🔎 THEORY: Flat File Storage

Before databases, applications used **flat files** like `.txt` or `.csv` to store data.
This method works for small, simple tasks but fails when data grows or multiple users need access.

A few problems with flat files:
- ❌ Hard to enforce structure or constraints
- ❌ Inefficient for querying large datasets
- ❌ No concurrency handling

This script simulates a primitive file-based data storage system.
"""

import json
import os

DATA_FILE = "users_data.txt"


def save_user(username, email):
    """Appends a user record to a plain text file (primitive storage)."""
    with open(DATA_FILE, "a") as f:
        record = json.dumps({"username": username, "email": email})
        f.write(record + "\n")


def read_users():
    """Reads and parses user records from the file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return [json.loads(line.strip()) for line in f if line.strip()]


def main():
    print("➡️ Simulating file-based data recording...")
    save_user("alice", "alice@example.com")
    save_user("bob", "bob@example.com")

    print("\n📄 Current users in file:")
    for user in read_users():
        print(f"- {user['username']} ({user['email']})")


if __name__ == "__main__":
    main()
