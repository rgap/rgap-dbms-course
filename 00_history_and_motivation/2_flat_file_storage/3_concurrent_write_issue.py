"""
⚠️ THEORY: Concurrency Problems in Flat File Systems

Flat files do not support concurrent writes safely.
If two threads/processes try to write to the same file at the same time,
they might overwrite or corrupt each other's data.

Modern DBMS solve this using **locks**, **journaling**, and **ACID transactions**.
This demo simulates two threads writing user records at the same time.

You may observe:
- Missing or overlapping lines
- Garbled output
- Random corruption

🧪 WHAT TO EXPECT AFTER RUNNING:
- You may see inconsistent write order (e.g., alice-alice-bob-alice-bob-bob)
- Sometimes, the records will appear incomplete or malformed
- Results vary each time due to thread interleaving

🚫 This wouldn't happen in a real DBMS:
- A transactional database would isolate each write with **row locks or table locks**
- It would write to a **write-ahead log (WAL)** before committing
- It would ensure **atomicity** — either the full record is written or none at all

This demonstrates the need for proper concurrency control in persistent systems.
"""

import json
import random
import threading
import time

DATA_FILE = "concurrent_users.txt"


def write_user(username):
    """Simulates writing a record to a shared file."""
    for _ in range(10):
        record = json.dumps({"username": username, "timestamp": time.time()})
        with open(DATA_FILE, "a") as f:
            f.write(record + "\n")
        time.sleep(random.uniform(0.01, 0.1))  # Random delay


def main():
    print("⚠️ Starting concurrent writes to the same file...\n")

    open(DATA_FILE, "w").close()  # Clear file first

    t1 = threading.Thread(target=write_user, args=("alice",))
    t2 = threading.Thread(target=write_user, args=("bob",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("\n✅ Done. Check the file for possible corruption:")
    print(f"{DATA_FILE}")


if __name__ == "__main__":
    main()
