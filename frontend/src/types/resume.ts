interface StandardizeResumeOutEducation {
    degree: string;
    major: string;
    school: string;
    start: string;
    end: string;
}

interface StandardizeResumeOutExperience {
    title: string;
    company: string;
    start: string;
    end: string | undefined;
    description: string;
}

interface StandardizeResumeOut {
    summary?: string;
    education?: StandardizeResumeOutEducation[];
    experience?: StandardizeResumeOutExperience[];
    skills?: string[];
    certifications?: string[];
    languages?: string[];
    publications?: string[];
}

export interface ResumeEditProps {
    resume: StandardizeResumeOut;
}