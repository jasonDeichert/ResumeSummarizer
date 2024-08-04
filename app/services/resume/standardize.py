import json
from typing import LiteralString
from openai.types.chat.chat_completion import ChatCompletion
from app.model.api.out import StandardizeResumeOut
from app.model.db.pdf import Text_Section_and_Style
from app.services.client import Client

async def standardize_resume(resume_content: list[Text_Section_and_Style], client: Client) -> StandardizeResumeOut:
    system_content: LiteralString = f'''You are an AI model that standardizes resumes.
    You will receive a list of objects with the following schema: {{"text_section": str, "size": float, "font": font-type, "color": color}}.
    Your job is to group the content into its logical categories.
    Use only the following categories: summary, education, experience, skills, certifications, languages, publications.
    The Education category should be a list of schema: {{"degree": str, "major": str, "school": str, "start": str, "end": str}}. All of these keys are optional if the resume does not include them.
    The Experience category should be list of schema: {{"title": str, "company": str, "start": str, "end": str, "description": str}}. All of these keys are optional if the resume does not include them.
    The Skills, Certifications, Languages, and Publications categories should be lists of strings.
    Return a JSON object with the categories as keys and the appropriate text content combined into one string (with the exception of experience and education) as the value. Don't include categories that do not appear in the resume.
    If you must use a different category, please provide a justification for doing so as a final key in the resume JSON object.'''
    
    user_content: str = f'''Standardize this resume: {resume_content}.'''
    
    completion: ChatCompletion = await client.client.chat.completions.create(
        model="gpt-4o",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    )
    
    message_content: str | None = completion.choices[0].message.content
    if message_content is None:
        raise ValueError("No message content returned from OpenAI")
    
    json_content = json.loads(message_content)
    return json_content