import React, { useState } from "react";

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
            const fileSize = file.size;
            console.log("File size:", fileSize);
            // Upload the file
            console.log("Uploading file:", file);
        } else {
            console.log("No file selected");
        }
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
                    accept = "application/pdf"
                    onChange={handleFileChange}
                    className="border border-gray-300 rounded-md p-2"
                />
            </div>
            <button
                type="submit"
                className="bg-blue-500 text-white py-2 px-4 rounded-md hover:bg-blue-600"
            >
                Upload
            </button>
        </form>
    );
};

export default PdfUploadForm;

