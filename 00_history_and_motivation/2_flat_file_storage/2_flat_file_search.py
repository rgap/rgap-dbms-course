"""
🔎 THEORY: Searching in flat files is expensive and inflexible.

In flat-file systems, you typically scan every line to find matching data.
This is called a **full scan** — it becomes slower as the file grows.

A DBMS uses **indexes** (e.g., B+ trees or hash maps) to quickly locate data.
This script illustrates why manual scanning is a bottleneck.

📊 TIME COMPLEXITY
- Flat file search: O(n) — must check every record
- Indexed search (e.g., B+ Tree): O(log n)

📈 SAMPLE PERFORMANCE (SIMULATED)
| Dataset Size   | Flat File Scan Time (s) | Indexed Time (estimated) |
|----------------|--------------------------|---------------------------|
| 100 records    | ~0.004                   | ~0.001                    |
| 1,000 records  | ~0.020                   | ~0.001                    |
| 10,000 records | ~0.200                   | ~0.001                    |
| 100,000 records| ~2.1                     | ~0.001                    |

➡️ Lesson: Even a simple lookup becomes costly as data grows without indexing.
"""

import json
import time

DATA_FILE = "users_data.txt"


def search_users_by_email(domain):
    """
    Manually scan the file to find users by email domain.

    ⚠️ Simulates a linear scan — for every record, we parse JSON and
    check the 'email' field. This works, but scales poorly.
    """
    matches = []
    with open(DATA_FILE, "r") as f:
        for line in f:
            if line.strip():
                user = json.loads(line.strip())
                if user["email"].endswith(domain):
                    matches.append(user)
    return matches


def main():
    domain = "@example.com"
    print(f"🔍 Searching for users with email domain '{domain}'...\n")

    start = time.time()
    results = search_users_by_email(domain)
    end = time.time()

    for user in results:
        print(f"✅ Found: {user['username']} ({user['email']})")

    print(f"\n⏱️ Search completed in {end - start:.4f} seconds")


if __name__ == "__main__":
    main()
