from fastapi import APIRouter, HTTPException, Depends
import app.controller.resume as resume_controller
from app.model.api.out import StandardizeResumeOut

router = APIRouter()

@router.post("/standardizeresume", response_model=StandardizeResumeOut)
async def standardize_resume(resume: str = Depends(resume_controller.standardize_resume)):
    return resume
