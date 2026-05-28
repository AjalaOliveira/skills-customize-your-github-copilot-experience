# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI and Pydantic to practice creating endpoints, request validation, and structured JSON responses.

## 📝 Tasks

### 🛠️ Create the REST API Endpoints

#### Description

Set up a FastAPI application with basic CRUD endpoints for managing products.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`
- Add endpoints for `GET /items`, `GET /items/{item_id}`, `POST /items`, `PUT /items/{item_id}`, and `DELETE /items/{item_id}`
- Store item data in an in-memory list or dictionary

### 🛠️ Define Pydantic Models

#### Description

Use Pydantic models to validate incoming request data and define the structure of API responses.

#### Requirements
Completed program should:

- Define a request model for creating and updating items
- Define a response model for item data
- Use the models in endpoint function signatures

### 🛠️ Add Validation and Error Handling

#### Description

Implement API validation and error handling to return correct HTTP status codes and messages.

#### Requirements
Completed program should:

- Validate required fields and data types using Pydantic
- Return `HTTPException(status_code=404)` when an item is not found
- Return `HTTPException(status_code=400)` for invalid update data when needed
- Provide clear JSON error messages

#### Example Request

```http
POST /items
Content-Type: application/json

{
  "name": "Notebook",
  "description": "A portable notebook",
  "price": 12.99
}
```
