import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

const UploadData = () => {
  const [file, setFile] = useState(null);
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a file to upload.');
      return;
    }

    const formData = new FormData();
    formData.append('data_file', file);

    try {
      const response = await fetch('/api/iv-data/upload/', {
        method: 'POST',
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`,
        },
        body: formData,
      });

      if (response.ok) {
        navigate('/dashboard');
      } else {
        const data = await response.json();
        setError(data.error);
      }
    } catch {
      setError('Error uploading file. Please try again.');
    }
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Upload IV Data</h2>
      <input type="file" onChange={handleFileChange} className="mb-4" />
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button onClick={handleUpload} className="bg-blue-500 text-white px-4 py-2 rounded">
        Upload
      </button>
    </div>
  );
};

export default UploadData;
