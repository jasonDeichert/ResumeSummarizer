import React, { useState, Dispatch, SetStateAction } from "react";
import {StandardizeResumeOut} from '../../types/resume';

interface PdfUploadFormProps {
    setIsResumeFileUploaded: Dispatch<SetStateAction<boolean>>;
    setResume: Dispatch<SetStateAction<StandardizeResumeOut>>;
}

const PdfUploadForm: React.FC<PdfUploadFormProps> = ({setIsResumeFileUploaded, setResume}) => {
    const [file, setFile] = useState<File | null>(null);

    const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const selectedFile = event.target.files?.[0] || null;
        setFile(selectedFile);
    };

    const [isLoading, setIsLoading] = React.useState<boolean>(false);


    const handleSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
        event.preventDefault();
        setIsLoading(true);
        if (file) {
            const formData = new FormData();
            formData.append("file", file);

            try {
                const response = await fetch("http://localhost:8000/standardizeresume", {
                    method: "POST",
                    body: formData,
                });

                if (response.ok) {
                    const data = await response.json();
                    console.log("API response:", data);
                    // Update the resume state with the response data
                    setIsResumeFileUploaded(true);
                    setResume(data);
                } else {
                    console.log("API request failed");
                }
            } catch (error) {
                console.log("API request error:", error);
            }
        } else {
            console.log("No file selected");
        }
        setIsLoading(false);
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-6">
            <div className="flex flex-col space-y-2">
                <label htmlFor="resumeFile" className="text-lg font-medium text-gray-700">
                    Upload Resume (PDF)
                </label>
                <input
                    type="file"
                    name="resumeFile"
                    id="resumeFile"
                    accept="application/pdf"
                    onChange={handleFileChange}
                    className="border border-gray-300 rounded-md p-2"
                />
            </div>
            <div className="flex justify-center">
                <button
                    type="submit"
                    className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600 flex items-center justify-center"
                >
                    {isLoading ? (
                        <div className="animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-white"></div>
                    ) : (
                        "Upload"
                    )}
                </button>
            </div>
        </form>
    );
    
};

export default PdfUploadForm;

