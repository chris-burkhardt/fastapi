# ⚡ FastAPI Exploration Project

This is a small project I built while exploring FastAPI. It includes:

- A few simple endpoints  
- Simple CRUD operations using an in-memory list  
- Enum-based routing  
- All logic kept in a single `main.py` file for simplicity during experimentation

For real-world use, I’d break this out into a more modular structure with separate files for routes, services, and data models to follow a modern backend architecture.

---

## 🚀 Features

- Path parameters with type validation  
- Enum-based route handling  
- Query string support  
- CRUD operations (Create, Read, Update, Delete) using a plain Python list  
- Interactive API docs via Swagger UI (`/docs`) and ReDoc (`/redoc`)

---

## 🔧 Virtual Environment Setup (FastAPI)

To isolate project dependencies, use a Python virtual environment.

1. **Create the virtual environment**  
   ```bash
   python -m venv venv
   ```

2. **Activate it**  
   - **macOS/Linux**:  
     ```bash
     source venv/bin/activate
     ```
   - **Windows**:  
     ```bash
     .\venv\Scripts\activate
     ```

3. **Confirm activation**  
   Your terminal prompt should now begin with `(venv)`.

4. **Install dependencies**  
   Example `requirements.txt`:
   ```
   fastapi[standard,dev]
   watchfiles
   ```
   Then install:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧩 VS Code Integration

1. Open Command Palette: `Cmd+Shift+P` (macOS) or `Ctrl+Shift+P` (Windows/Linux)  
2. Select:
   ```
   Python: Select Interpreter
   ```
3. Choose the one inside your `.venv` folder

> 💡 If your environment doesn't appear, activate it in your terminal before opening VS Code.

---

## ▶️ Running the App

Use Uvicorn (recommended development server):

```bash
uvicorn main:app --reload
```

Then open:
- [http://127.0.0.1:8000](http://127.0.0.1:8000) – base route
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) – Swagger UI
- [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc) – ReDoc UI

---

## 📁 Project Scope

All logic is in a single `main.py` file to keep things simple during development.  
To make it production-ready, I would split it into a modular layout like:

```
app/
├── __init__.py
├── main.py                 # Initializes FastAPI app and includes routers
├── api/                    # All route logic (organized by domain)
│   ├── __init__.py
│   ├── users.py
│   └── items.py
├── models/                 # Pydantic models and/or DB schemas
│   ├── __init__.py
│   ├── user.py
│   └── item.py
├── services/               # Business logic, separate from routes
│   ├── __init__.py
│   ├── user_service.py
│   └── item_service.py
├── db/                     # DB connection, session, and setup
│   ├── __init__.py
│   └── database.py
├── core/                   # Configuration, environment, shared dependencies
│   ├── __init__.py
│   └── config.py

tests/                      # Unit & integration tests
├── __init__.py
├── test_users.py
└── test_items.py

.env                        # Environment variables (optional)
requirements.txt            # Dependencies
README.md                   # Project documentation

```

---

## 📚 Based On

Official FastAPI Tutorial:  
https://fastapi.tiangolo.com/tutorial/
