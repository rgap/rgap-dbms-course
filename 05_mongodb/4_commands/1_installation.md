# 🧩 MongoDB Installation on macOS (Homebrew)

This guide walks you through installing **MongoDB Community Edition 8.0** on macOS using **Homebrew**, the macOS package manager.

---

## ✅ Prerequisites

Before installing MongoDB, make sure you have **Xcode Command Line Tools**, which are required for Homebrew and compiling dependencies.

```bash
xcode-select --install
```

This will prompt an installer window. Follow the on-screen instructions. If you already have it installed, you'll see a message saying it's already installed.

---

## 🍺 Step 1: Add the MongoDB Homebrew Tap

MongoDB provides its own Homebrew tap (a custom repository). Add it with:

```bash
brew tap mongodb/brew
```

This allows Homebrew to find and install the official MongoDB formula and tools.

---

## 🔄 Step 2: Update Homebrew

Make sure your Homebrew is up-to-date with the latest package definitions:

```bash
brew update
```

---

## 📦 Step 3: Install MongoDB Community Edition

Now, install MongoDB Community Edition version 8.0:

```bash
brew install mongodb-community@8.0
```

This installs:

- The MongoDB server
- The `mongosh` shell
- The tools required to manage MongoDB instances

---

## 🚀 Step 4: Start MongoDB as a macOS Service

To ensure MongoDB runs in the background and starts on boot:

```bash
brew services start mongodb-community@8.0
```

This uses `launchd` to run MongoDB as a background service.

---

## 🛑 Stop the MongoDB Service

If you want to stop the MongoDB server:

```bash
brew services stop mongodb-community@8.0
```

---

## 📋 View Running Services

To check if MongoDB is running, use:

```bash
brew services list
```

Look for `mongodb-community@8.0` in the list. If it says `started`, it's currently running.

---

## 🧠 Step 5: Access the MongoDB Shell

To interact with your database, use the **MongoDB Shell (`mongosh`)**:

```bash
mongosh
```

You’ll enter an interactive shell where you can run MongoDB commands.

Example:

```js
show dbs
```
