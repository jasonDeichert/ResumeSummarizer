import fitz # type: ignore
#this seems like it takes a long time to load the first time it's imported. We should try to make sure this is done when api service starts to avoid a slow first user xp.
from app.model.db.pdf import Text_Section_and_Style
from typing import List, BinaryIO

class Parse_PDF:
    def __init__(self, pdf_file: BinaryIO) -> None:
        self.pdf_file: BinaryIO = pdf_file
        self.pdf_object: fitz.Document = self.deserialize_pdf(pdf_file)
        self.text_content_and_styles: List[Text_Section_and_Style] = self.extract_text_content_and_styles(self.pdf_object)

    def deserialize_pdf(self, pdf_file: BinaryIO) -> fitz.Document:
        pdf_object: fitz.Document = fitz.open(stream=pdf_file.read(), filetype="pdf")
        return pdf_object

    def extract_text_content_and_styles(self, pdf_object: fitz.Document) -> List[Text_Section_and_Style]:
        text_content_and_styles: List[Text_Section_and_Style] = []
                
        for page_num in range(len(pdf_object)):
            page = pdf_object.load_page(page_num)  # type: ignore
            blocks = page.get_text("dict")["blocks"]  # type: ignore

            for block in blocks:  # type: ignore
                if "lines" in block:
                    for line in block["lines"]:  # type: ignore
                        for span in line["spans"]:  # type: ignore
                            text_content_and_styles.append(Text_Section_and_Style(
                                text=span["text"], # type: ignore
                                size=span["size"], # type: ignore
                                font=span["font"], # type: ignore
                                color=str(span["color"]) # type: ignore
                            ))  # type: ignore

        return text_content_and_styles
