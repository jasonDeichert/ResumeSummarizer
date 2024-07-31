//a component for the resumeedit page exclusively as of now.
//this component is used to upload the resume in pdf format.

import React, { useState } from "react";
import { Button, Form, FormGroup, Label, Input, FormText } from "reactstrap";

const PdfUploadForm = () => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = event.target.files?.[0] || null;
        setFile(selectedFile);
    };

    const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        // Handle file upload logic here
        if (file) {
            // Upload the file
            console.log("Uploading file:", file);
        } else {
            console.log("No file selected");
        }
    };

    return (
        <Form onSubmit={handleSubmit}>
            <FormGroup>
                <Label for="resumeFile">Upload Resume (PDF)</Label>
                <Input
                    type="file"
                    name="resumeFile"
                    id="resumeFile"
                    accept=".pdf"
                    onChange={handleFileChange}
                />
                <FormText color="muted">
                    Please upload your resume in PDF format.
                </FormText>
            </FormGroup>
            <Button type="submit" color="primary">
                Upload
            </Button>
        </Form>
    );
};

export default PdfUploadForm;

