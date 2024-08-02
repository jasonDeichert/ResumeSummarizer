import React from 'react';

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

interface ResumeEditProps {
    resume: StandardizeResumeOut;
}

const ResumeEdit: React.FC<ResumeEditProps> = ({ resume }) => {
    return (
        <div className="space-y-8">
            <h2 className="text-2xl font-bold mb-4">Experience</h2>
            {resume.experience?.map((experience, index) => (
                <div key={index} className="mb-4 p-4 border border-gray-200 rounded-lg shadow-sm">
                    <h3 className="text-xl font-semibold">{experience.title}</h3>
                    <p className="text-gray-700">{experience.company}</p>
                    <p className="text-gray-500">{experience.start} - {experience.end}</p>
                    <p className="text-gray-600">{experience.description}</p>
                </div>
            ))}

            <h2 className="text-2xl font-bold mb-4">Skills</h2>
            <ul className="list-disc list-inside space-y-2">
                {resume.skills?.map((skill, index) => (
                    <li key={index} className="text-gray-700">{skill}</li>
                ))}
            </ul>

            <h2 className="text-2xl font-bold mb-4">Certifications</h2>
            <ul className="list-disc list-inside space-y-2">
                {resume.certifications?.map((certification, index) => (
                    <li key={index} className="text-gray-700">{certification}</li>
                ))}
            </ul>

            <h2 className="text-2xl font-bold mb-4">Languages</h2>
            <ul className="list-disc list-inside space-y-2">
                {resume.languages?.map((language, index) => (
                    <li key={index} className="text-gray-700">{language}</li>
                ))}
            </ul>

            <h2 className="text-2xl font-bold mb-4">Publications</h2>
            <ul className="list-disc list-inside space-y-2">
                {resume.publications?.map((publication, index) => (
                    <li key={index} className="text-gray-700">{publication}</li>
                ))}
            </ul>
        </div>
    );
};

export default ResumeEdit;