from app.model.api.out import StandardizeResumeOut, SummarizeResumeOut
from app.model.db.resume import Resume, ResumeEducation, ResumeExperience, AISummary

# Assuming the models are already defined as provided

def convert_api_standardized_to_db_standardized(standardized_resume: StandardizeResumeOut) -> Resume:
    # Convert education
    education: list[ResumeEducation] = [
        ResumeEducation(
            degree=edu.degree,
            major=edu.major,
            school=edu.school,
            start=edu.start,
            end=edu.end
        ) for edu in (standardized_resume.education or [])
    ]
    
    # Convert experience
    experience: list[ResumeExperience] = [
        ResumeExperience(
            title=exp.title,
            company=exp.company,
            start=exp.start,
            end=exp.end,
            description=exp.description
        ) for exp in (standardized_resume.experience or [])
    ]
    
    # Create Resume object
    resume = Resume(
        summary=standardized_resume.summary,
        education=education if education else None,
        experience=experience if experience else None,
        skills=standardized_resume.skills,
        certifications=standardized_resume.certifications,
        languages=standardized_resume.languages,
        publications=standardized_resume.publications
    )
    
    return resume

def convert_api_summary_to_db_summary(api_summary: SummarizeResumeOut) -> AISummary:
    # Create AISummary object
    ai_summary = AISummary(
        quick_summary=api_summary.quick_summary,
        general_employability_rating=api_summary.general_employability_rating
    )
    
    return ai_summary