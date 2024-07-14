import fitz #this seems like it takes a long time to load the first time it's imported. We should try to make sure this is done when api service starts to avoid a slow first user xp.

class Parse_PDF:
    def __init__(self, pdf_file: str):
        self.pdf_file: str = pdf_file
        self.pdf_object: fitz.Document = self.deserialize_pdf(pdf_file)
        self.sections: list[dict] = self.extract_sections(self.pdf_object)

    def deserialize_pdf(self, pdf_file: str) -> fitz.Document:
        pdf_object = fitz.open(pdf_file)
        return pdf_object
    def extract_sections(self, pdf_object: fitz.Document) -> dict:
        sections = {}
        #text_info = [] #I'm not sure if we'll need this. I'm just keeping it here for now.
                
        for page_num in range(len(pdf_object)):
            page = pdf_object.load_page(page_num)
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" in block:
                    for line in block["lines"]:
                        for span in line["spans"]:
                            if span["size"] >= 14: #I'll need to test this on a few more common formats. Seems fine for LinkedIn generated PDF.
                                sections[span["text"]] = ""
                                current_section = span["text"]
                                #text_info.append(span) See 2nd line of function for comment.
                            else:
                                if len(sections) > 0:
                                    sections[current_section] += span["text"] #This isn't good enough. Often these different spans are separate lines and need to have 
                                
        
        return sections


#request console input for pdf file path
pdf_file = input('Enter the path to the PDF file: ')
parse_pdf = Parse_PDF(pdf_file)
print(parse_pdf.sections)
pass