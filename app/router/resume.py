# app/router/resume.py
from fastapi import APIRouter, UploadFile, File, Depends
from app.controller import resume as resume_controller
from app.model.api.out import StandardizeResumeOut
from app.services.client import Client
from datetime import datetime

router = APIRouter()

@router.post("/standardizeresume", response_model=StandardizeResumeOut)
async def standardize_resume(file: UploadFile = File(...), client: Client = Depends(Client.get_client)) -> StandardizeResumeOut:
    print(f"Received request to standardize a resume: {datetime.now()}")
    return await resume_controller.standardize_resume(file, client)
