//page for candidates to review and edit resume. 
import React from 'react';
import PdfUploadForm from '../components/employeeResumeEdit/pdfUploadForm';

const EmployeeResumeEdit: React.FC = () => {
    return (
        <div>
            <h1>Resume Edit Page</h1>
            <PdfUploadForm />
        </div>
    );
};

export default EmployeeResumeEdit;