import React from "react";
import { Link } from "react-router-dom";

const Navbar = () => {
  return (
    <nav className="bg-blue-500 p-4">
      <ul className="flex space-x-4">
        <li><Link to="/dashboard" className="text-white">Dashboard</Link></li>
        <li><Link to="/upload" className="text-white">Upload Data</Link></li>
        <li><Link to="/diagnostics" className="text-white">Diagnostics</Link></li>
        <li><Link to="/billing" className="text-white">Billing</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
