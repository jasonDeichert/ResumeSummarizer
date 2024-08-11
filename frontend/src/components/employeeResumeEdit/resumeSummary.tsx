import React from 'react';
import { SummarizeResumeOut } from '../../types/resume';

const ResumeSummary: React.FC<SummarizeResumeOut> = ({ quick_summary, general_employability }) => {
    if (general_employability === null) {
        return <div>{quick_summary}</div>;
    }
    else if (general_employability > 0 && general_employability <= 10) {
        const fullStars = Math.floor(general_employability / 2);
        const halfStar = general_employability % 2 !== 0;
        const emptyStars = 5 - fullStars - (halfStar ? 1 : 0);
        return (
            <div>
                <p>{quick_summary}</p>
                <div>
                    {[...Array(fullStars)].map((_, index) => (
                        <span key={`full-${index}`}>&#9733;</span> // Full star
                    ))}
                    {halfStar && <span key="half">&#9734;</span>} 
                    {[...Array(emptyStars)].map((_, index) => (
                        <span key={`empty-${index}`}>&#9734;</span> // Empty star
                    ))}
                </div>
            </div>
        );
    }
    else {
        console.log("Invalid general_employability value:", general_employability);
        return null;
    }


};

export default ResumeSummary;