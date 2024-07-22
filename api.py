from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import quotes
import random

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def get_random_quote():
    return {"quote": random.choice(quotes)}
