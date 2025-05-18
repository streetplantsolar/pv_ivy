import React, { useEffect, useState } from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

const Dashboard = () => {
  const [diagnostics, setDiagnostics] = useState([]);

  useEffect(() => {
    const fetchDiagnostics = async () => {
      try {
        const response = await fetch('/api/diagnostics/', {
          headers: {
            Authorization: `Token ${localStorage.getItem('token')}`,
          },
        });
        const data = await response.json();
        setDiagnostics(data.reports);
      } catch (error) {
        console.error('Error fetching diagnostics:', error);
      }
    };
    fetchDiagnostics();
  }, []);

  const sampleData = [
    { name: 'Point 1', voltage: 5, current: 10 },
    { name: 'Point 2', voltage: 10, current: 15 },
    { name: 'Point 3', voltage: 15, current: 20 },
    { name: 'Point 4', voltage: 20, current: 25 },
  ];

  return (
    <div className="bg-white p-6 rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Dashboard</h2>

      <h3 className="font-semibold mb-2">IV Curve Data</h3>
      <ResponsiveContainer width="100%" height={300}>
        <LineChart data={sampleData}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="voltage" />
          <YAxis />
          <Tooltip />
          <Line type="monotone" dataKey="current" stroke="#82ca9d" />
        </LineChart>
      </ResponsiveContainer>

      <div className="mt-6">
        <h3 className="font-semibold mb-2">Diagnostic Reports</h3>
        {diagnostics.length > 0 ? (
          diagnostics.map((report, index) => (
            <div key={index} className="p-4 bg-gray-100 rounded mb-2">
              Report generated at: {report.generated_at}
            </div>
          ))
        ) : (
          <p>No reports available.</p>
        )}
      </div>
    </div>
  );
};

export default Dashboard;
