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
    Your job is to summarize this into a single paragraph and accompanying information that is succinct as possible, containing the most important information.
    Be generous in your interpretation - try to paint the candidate in a good light and highlight their work (and other) projects.
    Additionally, be generous with their general employability rating. Someone with a few years of experience should have a high rating.
    '''
    
    user_content: str = f'''Summarize this resume: {resume}.'''
    
    completion: ChatCompletion = await client.client.beta.chat.completions.parse(
        model="gpt-4o-2024-08-06",
        response_format=SummarizeResumeOut,
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ]
    )
    
    message_content: str | None = completion.choices[0].message.content
    if message_content is None:
        raise ValueError("No message content returned from OpenAI")
    
    json_content = json.loads(message_content)
    summary = SummarizeResumeOut(**json_content)
    return summary