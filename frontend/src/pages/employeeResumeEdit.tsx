//page for candidates to review and edit resume. 
import React from 'react';
import PdfUploadForm from '../components/employeeResumeEdit/pdfUploadForm';
import ResumeEdit from '../components/employeeResumeEdit/resumeEdit';
import ResumeSummary from '../components/employeeResumeEdit/resumeSummary';
import {StandardizeResumeOut, SummarizeResumeOut} from '../types/resume';

const EmployeeResumeEdit: React.FC = () => {
    const mockResume: StandardizeResumeOut = {
        summary: "Experienced software developer with a passion for creating innovative solutions.",
        education: [
            {
                degree: "Bachelor of Science",
                major: "Computer Science",
                school: "University of Example",
                start: "2015-09-01",
                end: "2019-06-01"
            }
        ],
        experience: [
            {
                title: "Software Developer",
                company: "Tech Company",
                start: "2019-07-01",
                end: "2021-08-01",
                description: "Developed and maintained web applications."
            },
            {
                title: "Senior Software Developer",
                company: "Another Tech Company",
                start: "2021-09-01",
                end: null,
                description: "Leading a team of developers to build scalable software solutions."
            }
        ],
        skills: ["JavaScript", "React", "Node.js"],
        certifications: ["Certified Kubernetes Administrator"],
        languages: ["English", "Spanish"],
        publications: ["How to Build Scalable Web Applications"]
    };

    const handleSummarize = async () => {
        try {
            const response = await fetch("http://localhost:8000/summarizeresume", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(resume),
            });
    
            if (response.ok) {
                const data: SummarizeResumeOut = await response.json();
                console.log("API response:", data);
                // Update the resume summary state with the response data
                setResumeSummary(data);
            } else {
                console.log("API request failed");
            }
        } catch (error) {
            console.log("API request error:", error);
        }
    };

    const [isResumeFileUploaded, setIsResumeFileUploaded] = React.useState<boolean>(false);
    const [resume, setResume] = React.useState<StandardizeResumeOut>(mockResume);
    const [resumeSummary, setResumeSummary] = React.useState<SummarizeResumeOut | null>(null);
    
    
    return (
        <div>
            <div className="bg-white shadow-md rounded-md p-4 mb-4">
                <PdfUploadForm setIsResumeFileUploaded={setIsResumeFileUploaded} setResume={setResume} />
            </div>
            {isResumeFileUploaded && (
                <div className="text-center"> {/* Add this div with text-center class */}
                    <button className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded" onClick={handleSummarize}>
                        Summarize Resume
                    </button>
                </div>
            )}
            {resumeSummary != null && (
                <div className="bg-white shadow-md rounded-md p-4 mb-4"> {/* Add this div with p-4 and mb-4 classes */}
                    <ResumeSummary quick_summary={resumeSummary.quick_summary} general_employability={resumeSummary.general_employability} />
                </div>
            )}

            <div className="bg-white shadow-md rounded-md p-4">
                <ResumeEdit resume={resume}/>
            </div>
        </div>
    );
};

export default EmployeeResumeEdit;