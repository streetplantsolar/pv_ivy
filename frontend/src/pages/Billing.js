import React, { useState } from 'react';

const Billing = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubscribe = async () => {
    setLoading(true);
    try {
      const response = await fetch('/api/billing/subscribe/', {
        method: 'POST',
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`,
        },
      });
      const data = await response.json();

      if (response.ok) {
        window.location.href = `https://checkout.stripe.com/pay/${data.sessionId}`;
      } else {
        setError(data.error);
      }
    } catch {
      setError('Failed to initiate subscription. Please try again.');
    }
    setLoading(false);
  };

  return (
    <div className="bg-white p-6 rounded-lg shadow-lg">
      <h2 className="text-xl font-bold mb-4">Billing & Subscription</h2>
      {error && <p className="text-red-500 mb-4">{error}</p>}
      <button
        onClick={handleSubscribe}
        className="bg-blue-500 text-white px-4 py-2 rounded"
        disabled={loading}
      >
        {loading ? 'Processing...' : 'Subscribe Now'}
      </button>
    </div>
  );
};

export default Billing;
