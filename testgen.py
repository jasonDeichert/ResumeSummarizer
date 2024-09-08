
from tests.pytest.testGen.resumePDFGen import generate_test_pdfs
import asyncio
from app.services.client import Client

challenging_resumes: list[str] = [
    "Resume includes a mix of creative and technical roles, such as a graphic designer with experience in software development.",
    "Resume with extensive job hopping across unrelated industries, e.g., from hospitality to finance to engineering.",
    "Resume with gaps in employment history, including volunteer work, freelance gigs, and self-employment.",
    "Resume that blends academic and professional experiences, such as a PhD candidate working as a part-time consultant.",
    "Resume that contains overlapping job roles, such as a person working as both a project manager and a data analyst simultaneously.",
    "Resume with non-traditional job titles or self-invented titles, such as 'Chief Happiness Officer' or 'Culture Evangelist.'",
    "Resume with heavy emphasis on skills and projects, but minimal traditional work experience, often seen in new graduates or career changers.",
    "Resume of a professional with extensive experience in a niche industry that doesn't fit well into standard job categories.",
    "Resume containing multiple part-time jobs or gigs, with no clear primary occupation, typical in the gig economy.",
    "Resume with a hybrid background, such as someone who has been both an artist and a scientist, with significant experience in both fields."
]

challenging_camp_staff_resumes: list[str] = [
    "Resume with a mix of unrelated volunteer experiences, such as working at a food bank and organizing tech meetups.",
    "Resume of an individual with extensive experience in high-pressure corporate roles but minimal experience working with children.",
    "Resume with significant international experience, including teaching abroad, but no direct experience in outdoor or camp environments.",
    "Resume with a heavy focus on academic achievements and tutoring, but little to no hands-on or outdoor experience.",
    "Resume of a candidate with a background in competitive sports coaching, but no experience in non-competitive, recreational activities.",
    "Resume that lists experience in arts and crafts or theater, but with no mention of leadership or group management skills.",
    "Resume of someone who has worked primarily with older teenagers or adults, with little experience engaging with younger children.",
    "Resume with a background in special education or therapy, which might not align with general camp activities but could be valuable in certain contexts.",
    "Resume of a person with extensive leadership experience in corporate settings but no demonstrated ability to work in informal, flexible environments like a camp.",
    "Resume featuring a broad range of short-term, unrelated jobs, such as retail, fast food, and office work, without clear camp-related skills."
]

challenging_resumes_technical = [
    "Resume written in broken or non-standard English, with inconsistent grammar and spelling errors.",
    "Resume that uses non-traditional formats, such as a table or multi-column layout, making it hard for parsers to extract information.",
    "Resume submitted as an image or scanned document, requiring OCR (Optical Character Recognition) to interpret the text.",
    "Resume with unusual or excessive use of special characters, symbols, or emojis that could confuse parsing algorithms.",
    "Resume that includes embedded hyperlinks or multimedia elements like videos or graphics, making text extraction difficult.",
    "Resume where the job titles and dates are embedded within paragraphs rather than listed in a structured format.",
    "Resume with inconsistent or unconventional ordering, such as listing hobbies and interests before work experience or education.",
    "Resume with extensive use of abbreviations, acronyms, or industry-specific jargon that could be ambiguous or misinterpreted.",
    "Resume that frequently switches between languages, leading to potential confusion in text recognition and categorization.",
    "Resume using decorative fonts, colors, or other stylistic elements that may interfere with text readability and parsing."
]


async def main() -> None:
    client = Client()
    challenging_resumes_task = asyncio.create_task(generate_test_pdfs(challenging_resumes, "generally_challenging", client))
    challenging_camp_staff_resumes_task = asyncio.create_task(generate_test_pdfs(challenging_camp_staff_resumes, "camp_challenging", client))
    challenging_technical_resumes_task = asyncio.create_task(generate_test_pdfs(challenging_resumes_technical, "technical_challenging", client))
    await challenging_resumes_task
    await challenging_camp_staff_resumes_task#only needed if you update example.pdf
    await challenging_technical_resumes_task

if __name__ == "__main__":
    asyncio.run(main()) 