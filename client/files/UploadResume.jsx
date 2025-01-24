import React, { useState } from 'react';
import axios from 'axios';

const UploadResume = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      setError("Please upload a resume file.");
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    setLoading(true);
    setError(null);
    
    try {
      const response = await axios.post('http://127.0.0.1:5000/api/analyze-resume', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      // Process response to display details and generated questions
      const { details, questions } = response.data;
      setResult({
        skills: details.Skills,
        activities: details.Activities,
        questions: questions,
      });
    } catch (err) {
      console.error("Error uploading file:", err);
      setError("An error occurred while analyzing the resume.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Upload Your Resume</h1>
      
      {/* Display any error message */}
      {error && <p style={{ color: 'red' }}>{error}</p>}
      
      {/* Resume upload form */}
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit" disabled={loading}>Analyze Resume</button>
      </form>

      {/* Loading spinner */}
      {loading && <p>Loading...</p>}

      {/* Display results if available */}
      {result && (
        <div>
          <h2>Extracted Details</h2>
          <h3>Skills:</h3>
          <ul>
            {result.skills.length > 0 ? (
              result.skills.map((skill, index) => <li key={index}>{skill}</li>)
            ) : (
              <li>No skills extracted</li>
            )}
          </ul>

          <h3>Activities:</h3>
          <ul>
            {result.activities.length > 0 ? (
              result.activities.map((activity, index) => <li key={index}>{activity}</li>)
            ) : (
              <li>No activities extracted</li>
            )}
          </ul>

          <h3>Generated Interview Questions:</h3>
          <ul>
            {result.questions.length > 0 ? (
              result.questions.map((question, index) => <li key={index}>{question}</li>)
            ) : (
              <li>No questions generated</li>
            )}
          </ul>
        </div>
      )}
    </div>
  );
};

export default UploadResume;
