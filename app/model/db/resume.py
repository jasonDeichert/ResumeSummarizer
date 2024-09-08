#No actual db for now but it makes sense to have an internal model for the resume which can mimic a potential db schema
from pydantic import BaseModel
from typing import List, Optional

class ResumeEducation(BaseModel):
    degree: Optional[str] = None
    major: Optional[str] = None
    school: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None

class ResumeExperience(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    start: Optional[str] = None
    end: Optional[str] = None
    description: Optional[str] = None

class AISummary(BaseModel):
    quick_summary: Optional[str] = None
    general_employability_rating: Optional[int] = None


class Resume(BaseModel):
    summary: Optional[str] = None
    education: Optional[List[ResumeEducation]] = None
    experience: Optional[List[ResumeExperience]] = None
    skills: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    publications: Optional[List[str]] = None

class SummarizedResume(BaseModel):
    resume: Resume
    ai_summary: AISummary



