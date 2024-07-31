from pydantic import BaseModel, Field, ValidationError, RootModel
from typing import List, Tuple, Union, Optional, Dict

class SummarizeResumeIn(BaseModel):
    resume: str
    