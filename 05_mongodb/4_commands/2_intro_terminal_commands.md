# 💻 Intro Terminal Commands for MongoDB

This guide introduces basic terminal commands to access and interact with MongoDB through the shell (`mongosh`), as well as verifying tool installation and working with Docker containers.

---

## 🟢 Start the MongoDB Shell Locally

```bash
mongosh
```

Starts the MongoDB shell (`mongosh`) using the default host (`localhost`) and port (`27017`).

**Output:**

```
Current Mongosh Log ID: ...
Connecting to: mongodb://127.0.0.1:27017/
Using MongoDB: 6.0.5
Using Mongosh: 1.8.0
```

📌 Use this when running MongoDB locally with **no access control enabled**.

🔍 **Why no username/password?**  
By default, MongoDB starts **without authentication enabled**, meaning you can access everything freely. This is fine for local development but **not secure for production**.

To require a login, you must enable access control and create a user (explained below).

---

## 🔒 Connect with Username and Password

```bash
mongosh -u admin -p secret --authenticationDatabase admin
```

Connects to MongoDB using authentication. The user `admin` must exist in the `admin` database.

**Output:**

```
Successfully connected to: mongodb://127.0.0.1:27017/
Logged in as: admin
```

📌 Use this after enabling authentication and creating the user. Here’s how to set that up:

---

### ⚙️ How to Enable Authentication in MongoDB

#### 1. Start MongoDB **without** `--auth` and connect:

```bash
mongod --dbpath /your/data/db
```

Then in another terminal:

```bash
mongosh
```

#### 2. Create the `admin` user:

```js
use admin

db.createUser({
  user: "admin",
  pwd: "secret",
  roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
})
```

#### 3. Restart MongoDB **with access control enabled**:

Stop the current process and restart MongoDB with `--auth`:

```bash
mongod --auth --dbpath /your/data/db
```

Now MongoDB requires authentication.

---

#### ✅ Test it with the shell:

```bash
mongosh -u admin -p secret --authenticationDatabase admin
```

This connects you as the `admin` user.

---

## 🌐 Connect to a Remote MongoDB Server

```bash
mongosh "mongodb://192.168.1.10:27017"
```

Connects to a MongoDB server running on a different machine (IP: 192.168.1.10).

**Output:**

```
Connecting to: mongodb://192.168.1.10:27017/
Using MongoDB: 5.0.3
```

📌 Useful for managing MongoDB on remote hosts within the same network or via VPN.

---

## 🔧 Full URI Format (Including Authentication and Database)

```bash
mongosh "mongodb://admin:secret@localhost:27017/mydb?authSource=admin"
```

A full connection string using credentials, target DB, and specifying the DB where the user is stored (`authSource`).

**Output:**

```
Successfully connected to: mongodb://localhost:27017/
Authenticated as: admin
```

📌 This is the preferred way to connect to production or Atlas databases with full connection strings.

---

## 🐳 Connect to MongoDB in a Docker Container

```bash
docker exec -it my_mongo_container mongosh
```

Runs the shell **inside a Docker container** named `my_mongo_container`.

**Output:**

```
Connecting to: mongodb://127.0.0.1:27017/ inside container
Using MongoDB: 6.0.5
```

📌 Use this to debug or inspect a running MongoDB container.

---

## 🧪 Check Tool Versions

```bash
mongosh --version
```

Returns the version of the `mongosh` shell.

```bash
mongoimport --version
mongodump --version
```

Return the versions of CLI tools used to **import/export** data and **backup** databases.

**Output Example:**

```
mongoimport version: 100.7.1
mongodump version: 100.7.1
```

📌 Use this to confirm tool availability and check compatibility.

---

## ❌ Exit the MongoDB Shell

```bash
exit
```

Ends the `mongosh` session and returns to your regular terminal prompt.

**Output:**

```
Bye!
```

📌 Always exit cleanly to ensure no sessions remain open in remote environments.
