# app/router/resume.py
from fastapi import APIRouter, UploadFile, File, Depends
from app.controller import resume as resume_controller
from app.model.api.out import StandardizeResumeOut, SummarizeResumeOut
from app.services.client import Client
from datetime import datetime

router = APIRouter()

#interestingly, fastAPI handles serialization. It was handled earlier but that was unnecessary
@router.post("/standardizeresume", response_model=StandardizeResumeOut)
async def standardize_resume(file: UploadFile = File(...), client: Client = Depends(Client.get_client)) -> StandardizeResumeOut:
    print(f"Received request to standardize a resume: {datetime.now()}")
    standardized_resume: StandardizeResumeOut = await resume_controller.standardize_resume(file, client)
    return standardized_resume

@router.post("/summarizeresume", response_model=SummarizeResumeOut)
async def summarize_resume(resume: StandardizeResumeOut, client: Client = Depends(Client.get_client)) -> SummarizeResumeOut:
    print(f"Received request to summarize a resume: {datetime.now()}")
    summarized_resume: SummarizeResumeOut = await resume_controller.summarize_resume(resume, client)
    return summarized_resume