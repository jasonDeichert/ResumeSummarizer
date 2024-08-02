import React from 'react';
import './styles/tailwind.css';
import EmployeeResumeEdit from './pages/employeeResumeEdit';

function App() {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full max-w-2xl">
        <EmployeeResumeEdit />
      </div>
    </div>
  );
}

export default App;
