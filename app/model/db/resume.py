#No actual db for now but it makes sense to have an internal model for the resume which can mimic a potential db schema
from pydantic import BaseModel, Field, ValidationError, RootModel
from typing import List, Tuple, Union, Optional, Dict

class ResumeEducation(BaseModel):
    degree: Optional[str]
    major: Optional[str]
    school: Optional[str]
    start: Optional[str]
    end: Optional[str]

class ResumeExperience(BaseModel):
    title: Optional[str]
    company: Optional[str]
    start: Optional[str]
    end: Optional[str]
    description: Optional[str]


class Resume(BaseModel):
    summary: Optional[str]
    education: Optional[List[ResumeEducation]]
    experience: Optional[List[ResumeExperience]]
    skills: Optional[List[str]]
    certifications: Optional[List[str]]
    languages: Optional[List[str]]
    publications: Optional[List[str]]

