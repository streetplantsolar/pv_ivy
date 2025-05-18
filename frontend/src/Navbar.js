import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div className="bg-blue-600 text-white p-4 flex justify-between">
      <h1 className="font-bold">PV Ivy</h1>
      <div>
        <Link to="/dashboard" className="mr-4">Dashboard</Link>
        <Link to="/upload" className="mr-4">Upload Data</Link>
        <Link to="/diagnostics" className="mr-4">Diagnostics</Link>
        <Link to="/billing">Billing</Link>
      </div>
    </div>
  );
};

export default Navbar;
