import React from 'react';

import {StandardizeResumeOut} from '../../types/resume';
interface Props {
    resume: StandardizeResumeOut;
}

const ResumeEdit: React.FC<Props> = ({ resume }) => {
    return (
        <div className="space-y-8">
            <h2 className="text-2xl font-bold mb-4">Summary</h2>
            <p className="text-gray-600">{resume.summary}</p>

            <h2 className="text-2xl font-bold mb-4">Education</h2>
            {resume.education?.map((education, index) => (
                <div key={index} className="mb-4 p-4 border border-gray-200 rounded-lg shadow-sm">
                    <h3 className="text-xl font-semibold">{education.degree}</h3>
                    <p className="text-gray-600">{education.major}</p>
                    <p className="text-gray-700">{education.school}</p>
                    <p className="text-gray-500">{education.start} - {education.end ?? null}</p>
                </div>
            ))}

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