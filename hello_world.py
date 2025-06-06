# Import FastAPI to create the API
from fastapi import FastAPI

# Import uvicorn to run the app
import uvicorn

# Create a FastAPI app instance
app = FastAPI(
    title="My First API",                      # Title shown in docs
    description="A simple API using FastAPI",  # Short description
    version="1.0.0"                            # Version info
)

# Define the root route (home page)
@app.get("/")  # Handles GET requests to "/"
def read_root():
    return {"message": "Hello World! Welcome to FastAPI"}  # JSON response

# Define a route that takes a name from the URL
@app.get("/hello/{name}")  # Handles GET requests like "/hello/Ali"
def greet_user(name: str):  # Takes 'name' from URL as a string
    return {"message": f"Hello, {name}!"}  # Personalized response

# This block runs the server if this file is executed directly
if __name__ == "__main__":
    # Start the server using uvicorn
    uvicorn.run("hello_world:app", host="127.0.0.1", port=8000, reload=True)
    # "hello_world" is the filename (without .py), "app" is the FastAPI instance
    # reload=True allows auto-reloading on code changes
