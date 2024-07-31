from pydantic import BaseModel, Field, ValidationError, RootModel
from typing import List, Tuple, Union, Optional, Dict

class StandardizeResumeOutEducation(BaseModel):
    degree: str
    major: str
    school: str
    start: str
    end: str

class StandardizeResumeOutExperience(BaseModel):
    title: str
    company: str
    start: str
    end: Optional[str]
    description: str


class StandardizeResumeOut(BaseModel):
    summary: Optional[str]
    education: Optional[List[StandardizeResumeOutEducation]]
    experience: Optional[List[StandardizeResumeOutExperience]]
    skills: Optional[List[str]]
    certifications: Optional[List[str]]
    languages: Optional[List[str]]
    publications: Optional[List[str]]