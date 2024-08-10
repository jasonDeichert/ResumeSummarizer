# app/router/resume.py
from fastapi import APIRouter, UploadFile, File, Depends
from app.controller import resume as resume_controller
from app.model.api.out import StandardizeResumeOut, SummarizeResumeOut
from app.services.client import Client
from datetime import datetime

router = APIRouter()

@router.post("/standardizeresume", response_model=StandardizeResumeOut)
async def standardize_resume(file: UploadFile = File(...), client: Client = Depends(Client.get_client)) -> StandardizeResumeOut:
    print(f"Received request to standardize a resume: {datetime.now()}")
    return await resume_controller.standardize_resume(file, client)

@router.post("/summarizeresume", response_model=SummarizeResumeOut)
async def summarize_resumse(resume: StandardizeResumeOut, client: Client = Depends(Client.get_client)) -> SummarizeResumeOut:
    print(f"Received request to summarize a resume: {datetime.now()}")
    return await resume_controller.summarize_resume(resume, client)