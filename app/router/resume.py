# app/router/resume.py
from fastapi import APIRouter, UploadFile, File, Depends
from app.controller import resume as resume_controller
from app.model.api.out import StandardizeResumeOut
from app.services.client import Client

router = APIRouter()

@router.post("/standardizeresume", response_model=StandardizeResumeOut)
async def standardize_resume(file: UploadFile = File(...), client: Client = Depends(Client.get_client)) -> StandardizeResumeOut:
    return await resume_controller.standardize_resume(file, client)
