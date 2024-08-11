
interface StandardizeResumeOutEducation {
    degree: string | null;
    major: string | null;
    school: string | null;
    start: string | null;
    end: string | null;
}

interface StandardizeResumeOutExperience {
    title?: string | null;
    company?: string | null;
    start: string | null;
    end: string | null;
    description: string | null;
}

export interface StandardizeResumeOut {
    summary?: string | null;
    education?: StandardizeResumeOutEducation[] | null;
    experience?: StandardizeResumeOutExperience[] | null;
    skills?: string[] | null;
    certifications?: string[] | null;
    languages?: string[] | null;
    publications?: string[] | null;
}


export interface SummarizeResumeOut {
    quick_summary: string | null;
    general_employability: number | null;
}