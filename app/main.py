# api will come later
# from fastapi import FastAPI
# from app.router import resume

# app = FastAPI()

# app.include_router(resume.router, tags=["summarizeRecipe"])

from utils.pdf import Parse_PDF
from services.resume.standardize import standardize_resume
import asyncio

async def main():
    pdf_file_location = input("Enter the path to the pdf file: ")
    parsed_pdf = Parse_PDF(pdf_file_location)
    resume = await standardize_resume(parsed_pdf.text_content_and_styles)
    print(resume)


asyncio.run(main())

