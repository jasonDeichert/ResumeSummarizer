from pydantic import BaseModel
from typing import List
class Text_Section_and_Style(BaseModel):
    text: str
    size: float
    font: str
    color: str

class PDF_Model(BaseModel):
    pdf_file_location: str
    text_content_and_styles: List[Text_Section_and_Style]

