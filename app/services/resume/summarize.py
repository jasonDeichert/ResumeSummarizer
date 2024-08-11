import json
from openai.types.chat.chat_completion import ChatCompletion
from app.model.api.out import SummarizeResumeOut, StandardizeResumeOut
from app.utils.describe_class import describe_class
from app.services.client import Client

async def summarize_resume(resume: StandardizeResumeOut, client: Client) -> SummarizeResumeOut:
    system_content: str = f'''You summarize resumes into as few words as possible for an employer. Be skeptical and honest (don't oversell the candidate).
    The summary will be used to quickly compare potential candidates and act as a quick introduction for employers doing many interviews.
    You will receive an object with the following schema:
    {describe_class(StandardizeResumeOut)}
    Your job is to summarize this into a single paragraph that is succinct as possible, containing the most important information.
    Give an idea of how much school or work experience they have in number of years.
    Return a JSON object with this schema:
    {describe_class(SummarizeResumeOut)}
    The average general employability rating should be 5 (out of 10), which would represent a first year university student that is generally prepared to work a summer job.'''
    
    user_content: str = f'''Summarize this resume: {resume}.'''
    
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