'''import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

print("Status Code:", response.status_code)
print("Response JSON:")
print(response.json())



import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "GenAI",
    "body": "Learning APIs is important",
    "userId": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())'''

from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()

# -------- GET API --------
@app.get("/")
def home():
    return {"message": "Welcome to my first REST API"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}   

# -------- POST API --------
class TextInput(BaseModel):
    text: str

@app.post("/analyze")
def analyze_text(data: TextInput):
    word_count = len(data.text.split())
    return {
        "original_text": data.text,
        "word_count": word_count
    }

