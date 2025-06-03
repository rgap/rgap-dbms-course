# 🛠️ MongoDB Development Tools Setup

MongoDB provides several official and third-party tools to help developers **interact with data**, **visualize structures**, and **manage collections** beyond the command-line experience.

This module walks through the setup and usage of key tools like **MongoDB Compass**, **Atlas**, and general environment preparation.

---

## 🧰 Tools Overview

| Tool                    | Description                                                            |
| ----------------------- | ---------------------------------------------------------------------- |
| MongoDB Compass         | GUI for MongoDB: visualizes databases, runs queries, manages documents |
| MongoDB Atlas           | Cloud-hosted MongoDB service: provisioning, scaling, backups           |
| mongoimport             | Command-line tool to import JSON/CSV data into collections             |
| Mongo Shell (`mongosh`) | Interactive shell for scripting and querying                           |

---

## 🖥️ Installing MongoDB Compass

1. Visit: [https://www.mongodb.com/try/download/compass](https://www.mongodb.com/try/download/compass)
2. Choose your OS (macOS, Windows, Linux)
3. Download and install

No login is required. Once installed, you can connect to a local instance using:

```
mongodb://localhost:27017
```

---

## ☁️ MongoDB Atlas (Optional)

1. Sign up at [https://www.mongodb.com/cloud/atlas](https://www.mongodb.com/cloud/atlas)
2. Create a free cluster
3. Add your IP to the IP Access List (security tab)
4. Create a database user with username/password
5. Connect via Compass or Shell using the provided connection string

Atlas is ideal for testing cloud deployments and remote collaboration.
