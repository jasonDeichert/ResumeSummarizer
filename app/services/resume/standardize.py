import json
from openai.types.chat.chat_completion import ChatCompletion
from app.model.api.out import StandardizeResumeOut
from app.model.db.pdf import Text_Section_and_Style
from app.utils.describe_class import describe_class
from app.services.client import Client

async def standardize_resume(resume_content: list[Text_Section_and_Style], client: Client) -> StandardizeResumeOut:
    system_content: str = f'''You standardize resumes.
    You will receive a list of objects with the following schema:
    {describe_class(Text_Section_and_Style)}
    Your job is to group the text content into its logical categories.
    Return a JSON object with this schema:
    {describe_class(StandardizeResumeOut)}
    Format dates as MM/YYYY.
    Try to organize the text content nicely. For instance, if someone breaks up a description into bullet points, add new line characters as appropriate.'''
    
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