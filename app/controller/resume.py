import app.services.resume.standardize as standardize_service
import app.services.resume.summarize as summarize_service
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
    standardize_resume_task: Awaitable[apimodelout.StandardizeResumeOut] = asyncio.create_task(standardize_service.standardize_resume(parsed_pdf.text_content_and_styles, client))
    standardize_resume: apimodelout.StandardizeResumeOut = await standardize_resume_task
    return standardize_resume

async def summarize_resume(resume: apimodelout.StandardizeResumeOut, client: Client) -> apimodelout.SummarizeResumeOut:
    summarize_resume_task: Awaitable[apimodelout.SummarizeResumeOut] = asyncio.create_task(summarize_service.summarize_resume(resume, client))
    summarize_resume: apimodelout.SummarizeResumeOut = await summarize_resume_task
    return summarize_resume