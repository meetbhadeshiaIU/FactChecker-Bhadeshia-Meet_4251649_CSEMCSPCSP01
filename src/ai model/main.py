from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import check_similarity_score
from pydantic import BaseModel

app = FastAPI()

# Allow frontend requests (e.g., from React or localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # or specify your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI!"}

# Define the input data model
class TextInput(BaseModel):
    message: str

@app.post("/api/data")
def get_data(input_data: TextInput):

    # Retrieve the news text from the request
    news1 = input_data.message
    # news1 = "A powerful earthquake struck Japan’s coast early Monday." # dummy text
    news2 = "Japan was hit by a strong quake off its eastern shore on Monday morning."
    similarity = check_similarity_score(news1, news2)
    print("similarity", similarity)
    text = "Its a fake news"
    if similarity >= 60:
        text = "Its correct news"
    return {"text": text}