from fastapi import FastAPI, Depends
from app.router import resume
from app.services.client import Client

client = Client()

app = FastAPI()
app.include_router(resume.router, tags=["summarizeRecipe"], dependencies=[Depends(client.get_client)])
