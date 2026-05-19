# BookFlow Library API  
## FastAPI Modular Routing & CRUD Operations

This project demonstrates how to organize FastAPI applications using `APIRouter` and perform CRUD (Create, Read, Update, Delete) operations for a library management system.

---

# Project Objective

The purpose of this experiment is to:

- Learn modular routing using FastAPI
- Separate public and admin APIs
- Perform CRUD operations
- Validate data using Pydantic
- Build scalable backend structure

---

# Technologies Used

- Python 3.14
- FastAPI
- Uvicorn
- Pydantic

---

# Project Structure

```text
Experiment6/
│
├── main.py
├── models.py
│
├── routes/
│   ├── __init__.py
│   ├── catalog.py
│   └── admin.py
```

---

# Features

## Public Catalog Routes

- View all books
- View single book details

## Admin Routes

- Add new books
- Update existing books
- Delete books

## Validation

- Prevent negative prices
- Validate ISBN as string

---

# Pre-Installation Commands

## Step 1 — Create Virtual Environment

```bash
python -m venv venv
```

---

## Step 2 — Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Step 3 — Install Required Packages

```bash
pip install fastapi uvicorn
```

---

# Run the Application

Use the following command:

```bash
python -m uvicorn main:app --reload
```

---

# Server URL

```text
http://127.0.0.1:8000
```

---

# Swagger Documentation

Open:

```text
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## Public Routes

### Get All Books

```http
GET /books
```

### Get Book by ID

```http
GET /books/{book_id}
```

---

## Admin Routes

### Add Book

```http
POST /admin/books
```

### Update Book

```http
PUT /admin/books/{book_id}
```

### Delete Book

```http
DELETE /admin/books/{book_id}
```

---

# Example Request Body

```json
{
  "id": 1,
  "title": "FastAPI Basics",
  "author": "Sai",
  "isbn": "ISBN101",
  "price": 500,
  "status": "Available"
}
```

---

# Validation Rules

| Field | Validation |
|---|---|
| price | Cannot be negative |
| isbn | Must be string |

---

# File Descriptions

## main.py

Main entry point of the FastAPI application.

Responsibilities:
- Create FastAPI app
- Include routers
- Start API service

---

## models.py

Contains Pydantic models for validation.

Responsibilities:
- Define Book schema
- Validate input data
- Prevent invalid requests

---

## routes/catalog.py

Contains public routes.

Responsibilities:
- View all books
- View specific book details

---

## routes/admin.py

Contains admin routes.

Responsibilities:
- Add books
- Update books
- Delete books

---

# CRUD Operations

| Method | Purpose |
|---|---|
| GET | Read data |
| POST | Create new data |
| PUT | Update existing data |
| DELETE | Remove data |

---

# Expected Learning Outcomes

- Understanding FastAPI Routers
- Modular backend architecture
- CRUD API implementation
- Request validation using Pydantic
- API testing using Swagger UI

---

# Result

Successfully implemented organized routing and CRUD operations using FastAPI with modular structure and validation.

---

# Author

Sai Teja,  2500030136,
DBMS Lab Experiment 6
