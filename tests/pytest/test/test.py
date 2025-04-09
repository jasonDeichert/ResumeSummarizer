import os

import app.services.resume.standardize as standardize_service
import app.services.resume.summarize as summarize_service
import app.model.api.out as apimodelout
import app.model.db.resume as db_resume_model
import app.model.db.pdf as db_pdf_model
from app.services.client import Client
from app.model._converter.api_to_db import convert_api_standardized_to_db_standardized, convert_api_summary_to_db_summary

client: Client = Client()

async def test_standardize_and_summarize_resume() -> None:
    # Path to the directory containing the serialized JSON files
    directory = 'tests/pytest/testGen/testpdfs'
    # Iterate through each file in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.json'):
            file_path = os.path.join(directory, filename)
            
            # Perform operations on the file
            with open(file_path, 'r') as file:
                serialized_json = file.read()
                
            # Deserialize the JSON file
            resume_pdf: db_pdf_model.PDF_Model = db_pdf_model.PDF_Model.model_validate_json(serialized_json)
            # Standardize the resume
            standardized_resume: apimodelout.StandardizeResumeOut = await standardize_service.standardize_resume(resume_pdf.text_content_and_styles, client)
            # Summarize the standardized resume
            summary: apimodelout.SummarizeResumeOut = await summarize_service.summarize_resume(standardized_resume, client)

            # Save the summarized resume to json files
            db_standardized_resume: db_resume_model.Resume = convert_api_standardized_to_db_standardized(standardized_resume)
            db_summary: db_resume_model.AISummary = convert_api_summary_to_db_summary(summary)
            resume_to_save = db_resume_model.SummarizedResume(resume=db_standardized_resume, ai_summary=db_summary)
            serialized_resume: str = resume_to_save.model_dump_json()
            with open(f'tests/pytest/test/results/{filename}', 'w') as file:
                file.write(serialized_resume)


            
            
            
            



