from enum import Enum
from typing import Optional, List
from fastapi import FastAPI, Query, Path, Body, HTTPException

# --- Enum for route demo ---
class ModelName(str, Enum):
    alexnet = "alexnet"
    model_b = "model_b"


app = FastAPI(title="FastAPI Sample Project", description="A professional demo app using FastAPI.")


# --- In-memory "database" ---
fake_users_db: List[dict] = [
    {"id": 1, "username": "alice", "email": "alice@example.com"},
    {"id": 2, "username": "bob", "email": "bob@example.com"},
]


@app.get("/", summary="Health check")
async def root() -> dict:
    """Simple health check endpoint."""
    return {"message": "Hello World!"}


@app.get("/items/{item_id}", summary="Get item by ID")
async def read_item(item_id: int) -> dict:
    """Return an item by its numeric ID."""
    return {"item_id": item_id}


@app.get("/search/", summary="Search items")
async def search_items(q: Optional[str] = Query(None, max_length=50)) -> dict:
    """Return search query or fallback message."""
    return {"query": q or "No query provided"}


@app.get("/users", summary="List all users")
async def get_users() -> List[dict]:
    """Retrieve all users in the database."""
    return fake_users_db


@app.get("/users/{user_id}", summary="Get user by ID")
async def read_user(user_id: int = Path(..., gt=0), detailed: bool = False) -> dict:
    """
    Retrieve a user by ID.
    Optionally include full details with `?detailed=true`.
    """
    user = next((u for u in fake_users_db if u["id"] == user_id), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user if detailed else {"username": user["username"]}


@app.post("/users", summary="Create new user")
async def create_user(user: dict = Body(...)) -> dict:
    """Add a new user to the in-memory database."""
    new_id = max([u["id"] for u in fake_users_db], default=0) + 1
    user["id"] = new_id
    fake_users_db.append(user)
    return user


@app.put("/users/{user_id}", summary="Update user")
async def update_user(user_id: int, updated: dict = Body(...)) -> dict:
    """Update user fields based on provided payload."""
    for user in fake_users_db:
        if user["id"] == user_id:
            user.update(updated)
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/users/{user_id}", summary="Delete user")
async def delete_user(user_id: int) -> dict:
    """Delete a user by ID."""
    for i, user in enumerate(fake_users_db):
        if user["id"] == user_id:
            return fake_users_db.pop(i)
    raise HTTPException(status_code=404, detail="User not found")


@app.get("/models/{model_name}", summary="Model info using Enum")
async def get_model(model_name: ModelName) -> dict:
    """Return a message based on the model name enum."""
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "This is the AlexNet model."}
    if model_name == ModelName.model_b:
        return {"model_name": model_name, "message": "This is Model B."}


@app.get("/model/dict/{model_name}", summary="Model info using dictionary")
async def get_model_dict(model_name: ModelName) -> dict:
    """Alternative model message handler using a mapping dictionary."""
    messages = {
        ModelName.alexnet: "This is the AlexNet model.",
        ModelName.model_b: "This is Model B."
    }
    return {"model_name": model_name, "message": messages[model_name]}
