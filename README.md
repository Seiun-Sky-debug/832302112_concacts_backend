# 832302112_concacts_backend
EE308-Assignment1-backend

# Contacts API Backend
This is the backend server for the "Contacts Management" application, part of the Software Engineering course assignment.

## Features
- Provides a RESTful API for contacts.

- Full CRUD (Create, Read, Update, Delete) operations.

- Built with FastAPI and Python 3.10+.

- Uses MongoDB with Beanie (Async ODM) for data persistence.

## Tech Stack
- **Framework:** FastAPI

- **Database:** MongoDB

- **ODM:** Beanie

- **Server:** Uvicorn / Gunicorn

## Local Development Setup
1.**Prerequisites:**
  - Python 3.10+
  - MongoDB Community Server (running locally on `localhost:27017`)
  - Git

2.**Clone the repository:**

```
  git clone [https://github.com/Seiun-Sky-debug/832302112_concacts_backend.git](https://github.com/Seiun-Sky-debug/832302112_concacts_backend.git)
  cd 832302112_concacts_backend
```


3.**Create and activate a virtual environment:**
```
# Windows
python -m venv venv
.\venv\Scripts\activate
```
```
# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

4.**Install dependencies:**

```
pip install -r requirements.txt
```

5.**Run the development server:**
```
uvicorn src.main:app --reload
```

6.**Access the API:**

- API Root: [API Root](http://127.0.0.1:8000/ "API Root")

- API Docs (Swagger): [API Docs](http://127.0.0.1:8000/docs "API Docs (Swagger)")
