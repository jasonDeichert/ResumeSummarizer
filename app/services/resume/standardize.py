from openai import AsyncOpenAI
import httpx
import json
import base64
from model.db.resume import Resume
from model.db.pdf import Text_Section_and_Style
from datetime import datetime
from typing import List

client = AsyncOpenAI(
  http_client=httpx.AsyncClient(
    limits=httpx.Limits(
      max_connections=1000,
      max_keepalive_connections=100
    )
  )
)

max_prompt_length = 50

async def standardize_resume(resume_content: list[Text_Section_and_Style])-> Resume:
  system_content =f'''You are an AI model that standardizes resumes.
  You will receive a list of objects with the following schema: {{"text_section": str, "size": float, "font": font-type, "color": color}}
  Your job is to group the content into its logical categories.
  Use only the following categories: summary, education, experience, skills, certifications, languages, publications.
  The Education category should be of schema: {{"degree": str, "major": str, "school": str, "start": str, "end": str}}. All of these keys are optional if the resume does not include them.
  The Experience category should be of schema: {{"title": str, "company": str, "start": str, "end": str, "description": str}}. All of these keys are optional if the resume does not include them.
  Return a JSON object with the categories as keys and the appropriate text content combined into one string (with the exception of experience and education) as the value. Don't include categories that do not appear in the resume.
  If you must use a different category, please provide a justification for doing so as a final key in the resume JSON object.'''

  user_content=f'''Standardize this resume: {resume_content}.'''

  completion = await client.chat.completions.create(
      model="gpt-4o",
      response_format={"type": "json_object"},
      messages=[
      {"role": "system", "content": system_content},
      {"role": "user", "content": user_content}
    ]
  )
  json_content =  json.loads(completion.choices[0].message.content)
  return json_content