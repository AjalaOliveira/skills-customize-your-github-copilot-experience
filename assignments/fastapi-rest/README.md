# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to design and implement a small REST API using the FastAPI framework, focusing on request/response models, routing, validation and basic error handling.

## 📝 Tasks

### 🛠️ Implement a Simple REST API

#### Description
Create a FastAPI application that exposes CRUD-like endpoints for a simple resource (for example, `items`). The API should validate input, return appropriate HTTP status codes, and handle basic error conditions.

#### Requirements
Completed project should:

- Provide a GET endpoint to list resources (e.g., `GET /items`).
- Provide a GET endpoint to retrieve a single resource by id (e.g., `GET /items/{id}`).
- Provide a POST endpoint to create a new resource with request validation (e.g., `POST /items`).
- Use Pydantic models for request/response validation and documentation.
- Return proper HTTP status codes and JSON responses for success and error cases.
- Include clear instructions to run the app locally (using `uvicorn`).

#### Example requests
```
GET /items
Response 200
[
  {"id": 1, "name": "Notebook", "price": 12.5}
]

POST /items
Request body:
{
  "name": "Pencil",
  "price": 1.2
}
Response 201
{ "id": 2, "name": "Pencil", "price": 1.2 }
```

### 🛠️ Optional: Extensions

#### Description
Add one or more optional features to make the API more production-like.

#### Requirements

- Add PUT or PATCH endpoints to update resources.
- Add basic pagination or filtering to the list endpoint.
- Persist data to a simple SQLite database using SQLModel or `sqlite3` (optional).
- Add simple authentication (token-based) to protect write endpoints.

---

Place your solution file(s) (e.g., `app.py`) in this folder alongside this `README.md`. To run locally:

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
