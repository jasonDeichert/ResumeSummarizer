import app.services.resume.standardize as s
from fastapi import UploadFile
import app.model.api.out as apimodelout
import asyncio
from app.utils.pdf import Parse_PDF
from typing import Awaitable, BinaryIO
from app.services.client import Client
from io import BytesIO

async def standardize_resume(file: UploadFile, client: Client) -> apimodelout.StandardizeResumeOut:
    #convert file to BinaryIO
    file_binary: BinaryIO = BytesIO(await file.read())
    parsed_pdf: Parse_PDF = Parse_PDF(file_binary)
    standardize_resume_task: Awaitable[apimodelout.StandardizeResumeOut] = asyncio.create_task(s.standardize_resume(parsed_pdf.text_content_and_styles, client))
    standardize_resume: apimodelout.StandardizeResumeOut = await standardize_resume_task
    return standardize_resume
