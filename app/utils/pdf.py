import fitz #this seems like it takes a long time to load the first time it's imported. We should try to make sure this is done when api service starts to avoid a slow first user xp.
from pydantic import BaseModel
from model.db.resume import ResumeEducation, ResumeExperience, Resume
from model.db.pdf import Text_Section_and_Style

class Parse_PDF:
    def __init__(self, pdf_file: str):
        self.pdf_file: str = pdf_file
        self.pdf_object: fitz.Document = self.deserialize_pdf(pdf_file)
        self.text_content_and_styles: list[dict] = self.extract_text_content_and_styles(self.pdf_object)

    #we should add some validation on document size
    def deserialize_pdf(self, pdf_file: str) -> fitz.Document:
        pdf_object = fitz.open(pdf_file)
        return pdf_object
    def extract_text_content_and_styles(self, pdf_object: fitz.Document) -> list[Text_Section_and_Style]:
        text_content_and_styles = []
                
        for page_num in range(len(pdf_object)):
            page = pdf_object.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            text_content_and_styles.append(Text_Section_and_Style(text = span["text"], size = span["size"], font = span["font"], color = str(span["color"]))) 

        return text_content_and_styles
