from pydantic import BaseModel

class SummarizeResumeIn(BaseModel):
    resume: str
    