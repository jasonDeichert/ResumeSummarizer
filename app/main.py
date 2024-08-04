from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.router import resume
from app.services.client import Client

client = Client()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins='http://localhost:3000/',
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(resume.router, tags=["summarizeRecipe"], dependencies=[Depends(client.get_client)])
