
from openai.types.chat.chat_completion import ChatCompletion
from app.model.db.pdf import Text_Section_and_Style
from app.utils.describe_class import describe_class
from app.services.client import Client
from app.utils.pdf import Parse_PDF
from app.model.db.pdf import PDF_Model
import io
import json


def create_example_parsed_pdf() -> None:
    file_path = "tests/pytest/testGen/example.pdf"
    with open(file_path, "rb") as file:
        binary_io = io.BytesIO(file.read())
    parsed_pdf = Parse_PDF(binary_io)
    pdf_model = PDF_Model(pdf_file_location=file_path, text_content_and_styles=parsed_pdf.text_content_and_styles)
    json_content: str = pdf_model.model_dump_json()
    with open("tests/pytest/testGen/example.json", "w") as file:
        file.write(json_content)

async def generate_test_resume_parsed_pdf(resume_description: str, client: Client) -> list[Text_Section_and_Style]:
    example_parsed_pdf_location: str = "tests/pytest/testGen/example.json"
    with open(example_parsed_pdf_location, "r") as file:
        example_parsed_pdf_json: str = file.read()
    parsed_pdf = json.loads(example_parsed_pdf_json)
    pdf_model = PDF_Model(pdf_file_location=example_parsed_pdf_location, text_content_and_styles=parsed_pdf['text_content_and_styles'])
    system_content: str = f'''You will receive a string of a resume description.
    Your job is to generate the text content from a parsed pdf based on the description.
    Return a JSON object with this schema:
    generated_resume: list[{describe_class(Text_Section_and_Style)}].
    Here is an example:
    generated_resume: {str(pdf_model.text_content_and_styles)}
    This is meant to test a resume standardizing algorithm. The resumes should be as realistic as possible, but push the boundaries of what the algorithm can handle.'''
    
    user_content: str = f'''Generate a test resume based on this description: {resume_description}.'''
    
    completion: ChatCompletion = await client.client.chat.completions.create(
        model="gpt-4o-mini",
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
    return json_content['generated_resume']

async def generate_test_pdfs(desciption_list: list[str], description_type: str, client: Client) -> None:
    resume_index = 0
    for description in desciption_list:
        parsed_pdf: list[Text_Section_and_Style] = await generate_test_resume_parsed_pdf(description, client)
        pdf_model = PDF_Model(pdf_file_location=f"tests/pytest/testGen/resume{resume_index}.json", text_content_and_styles=parsed_pdf)
        with open(f"tests/pytest/testGen/{description_type}.{resume_index}.json", "w") as file:
            file.write(pdf_model.model_dump_json())
        resume_index += 1
        print(f"Generated resume {resume_index} with description: {description}.")