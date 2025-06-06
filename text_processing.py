from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import uvicorn 

# Create FastAPI instance
app = FastAPI(title="Simple Text API",
              description="A simple text API to demonstrate FastAPI",
              version="1.0.0")

# Define a Pydantic model for the Request body
class TextRequest(BaseModel):
    text: str
    uppercase: Optional[bool] = False

# Define a Pydantic model for the Response body
class TextResponse(BaseModel):
    processed_text: str
    text_length: int

# Define a route (endpoint)
@app.get("/")
def read_root():
    return {"message": "Welcome to our Text Processing API!"}

# Define a POST endpoint to process the text
@app.post("/process-text/", response_model=TextResponse)
def process_text(request: TextRequest):
    text = request.text

    # Check if the text is empty
    if not text:
        raise HTTPException(status_code=400, detail="Text cannot be empty")
    
    # Process the text (Convert to uppercase if requested)
    processed_text = text.upper() if request.uppercase else text

    # Create the Response
    response = TextResponse(
        processed_text=processed_text,
        text_length=len(processed_text)
    )

    return response

# Run the server
if __name__ == "__main__":
    uvicorn.run("text_processing:app", host="127.0.0.1", port=8000, reload=True)
    # "text_processing" is the filename (without .py), "app" is the FastAPI instance
    # reload=True to reload the server when the code changes
