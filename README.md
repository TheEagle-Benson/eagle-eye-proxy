# 🦅 Eagle Eye Geocoding Proxy Server

A **secure**, **high‑performance** reverse proxy server built with **FastAPI** for the **Eagle Eye Navigation App**. This service safely handles geocoding requests to third‑party APIs, keeps your API keys hidden, and automatically falls back to free providers when needed.

---

## 🚀 Features

- 🔐 **Secure by Design** – OpenCage API key is stored using environment variables (never exposed to the frontend!).
- 🛡️ **Fail‑Safe Fallback** – If OpenCage errors or rate limits, requests automatically switch to Nominatim (OpenStreetMap).
- ⚡ **Fast & Async** – Built using **FastAPI** and **httpx** for efficient asynchronous request handling.
- 🌍 **CORS Enabled** – Configured to accept requests from Eagle Eye frontend application domains.

---

## 🧰 Tech Stack

- 🐍 **Python 3.8+**
- 🚀 **FastAPI** (REST API framework)
- 🌐 **httpx** (async HTTP client)
- 🔧 **python-dotenv** (local environment variable management)

---

## 🛠️ Getting Started (Local Development)

### ✅ Prerequisites

- Python 3.8+
- OpenCage API Key (free tier works)

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/TheEagle-Benson/eagle-eye-proxy
cd eagle-eye-proxy
```

### 2️⃣ Create & activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ Install project dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

Create a `.env` file in your project root and add your OpenCage API key:

```env
API_KEY="YOUR_OPENCAGE_API_KEY_HERE"
```

> 🔒 Ensure the `.env` file is listed in `.gitignore` so it never gets committed.

---

## ▶️ Running the Server

Start the FastAPI development server:

```bash
python main.py
```

The server will run at:

```
http://127.0.0.1:8000
```

You can visit the automatic API docs at:

```
http://127.0.0.1:8000/docs
```

---

## 🌐 Deployment

This proxy server is deployed as a **serverless function on Vercel**.

Live endpoint:

```
https://eagle-eye-proxy.vercel.app
```

When deploying anywhere (Vercel, Fly.io, Render, etc.):

- Add `API_KEY` to the hosting provider's environment variables panel.

---

## 📄 License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.

#

