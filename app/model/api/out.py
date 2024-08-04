from pydantic import BaseModel
from typing import List, Optional

class StandardizeResumeOutEducation(BaseModel):
    degree: str
    major: str
    school: str
    start: str
    end: Optional[str] = None

class StandardizeResumeOutExperience(BaseModel):
    title: str
    company: str
    start: str
    end: Optional[str] = None
    description: Optional[str] = None


class StandardizeResumeOut(BaseModel):
    summary: Optional[str] = None
    education: Optional[List[StandardizeResumeOutEducation]] = None
    experience: Optional[List[StandardizeResumeOutExperience]] = None
    skills: Optional[List[str]] = None
    certifications: Optional[List[str]] = None
    languages: Optional[List[str]] = None
    publications: Optional[List[str]] = None