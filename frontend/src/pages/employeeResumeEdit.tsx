//page for candidates to review and edit resume. 
import React from 'react';
import PdfUploadForm from '../components/employeeResumeEdit/pdfUploadForm';
import ResumeEdit from '../components/employeeResumeEdit/resumeEdit';
import {StandardizeResumeOut} from '../types/resume';

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
    const [isResumeFileUploaded, setIsResumeFileUploaded] = React.useState<boolean>(false);
    const [resume, setResume] = React.useState<StandardizeResumeOut>(mockResume);
    
    
    return (
        <div>
            <PdfUploadForm setIsResumeFileUploaded={setIsResumeFileUploaded} setResume={setResume} />
            <ResumeEdit resume={resume}/>
        </div>
    );
};

export default EmployeeResumeEdit;