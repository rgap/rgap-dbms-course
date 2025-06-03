"""
⚠️ THEORY: Concurrency Problems in Flat File Systems

Flat files do not support concurrent writes safely.
If two threads/processes try to write to the same file at the same time,
they might overwrite or corrupt each other's data.

Modern DBMS solve this using concurrency control mechanisms.
This demo simulates two threads writing user records at the same time.
"""

import random
import threading
import time

# This file simulates a flat-file "database" with no concurrency control.
DATA_FILE = "concurrent_user_inserts.txt"


def write_user(username):
    """
    Simulates repeated INSERT operations into a 'users' table.

    In SQL, this would be equivalent to running this 5 times:
        INSERT INTO users (username) VALUES ('alice');

    Each call represents one record being added.

    ❌ Without concurrency control:
    - Two users writing at the same time may produce mixed or corrupted data.
    - Flat files don't guarantee that one "insert" finishes before another starts.
    - Result: overlapping writes, interleaved characters, broken lines.

    ✅ In a DBMS:
    - Each INSERT is atomic and isolated.
    - Writes are protected with locks or transactions.
    - No mixing or data corruption would occur.
    """
    for _ in range(5):  # Simulate 5 INSERTS per user
        record = f"user:{username}\n"

        # Write each character individually to increase chance of interleaving
        for char in record:
            with open(DATA_FILE, "a") as f:
                # No lock — so other thread may write at the same time
                f.write(char)


def main():
    print("⚠️ Simulating concurrent INSERTs into a flat file (no locks)...\n")

    # Clear the file first
    open(DATA_FILE, "w").close()

    # Two users each performing 5 INSERTs concurrently
    t1 = threading.Thread(target=write_user, args=("alice",))
    t2 = threading.Thread(target=write_user, args=("bob",))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("\n✅ Finished. Check the file for corrupted or interleaved lines:")
    print(f"{DATA_FILE}")


if __name__ == "__main__":
    main()
