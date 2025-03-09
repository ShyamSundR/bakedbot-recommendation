import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [preferences, setPreferences] = useState('');
  const [recommendations, setRecommendations] = useState([]);
  const [productInfo, setProductInfo] = useState(null);

  const getRecommendations = async () => {
    try {
      const response = await axios.get('http://localhost:3000/recommendations', {
        params: { preferences },
      });
      setRecommendations(response.data);
    } catch (error) {
      console.error('Error fetching recommendations:', error);
    }
  };

  const getProductInfo = async (id) => {
    try {
      const response = await axios.get(`http://localhost:3000/product-info/${id}`);
      setProductInfo(response.data.augmentedInfo);
    } catch (error) {
      console.error('Error fetching product info:', error);
    }
  };

  return (
    <div>
      <h1>AI-Powered Product Recommendation</h1>
      <input 
        type="text" 
        placeholder="Enter preferences" 
        value={preferences} 
        onChange={(e) => setPreferences(e.target.value)} 
      />
      <button onClick={getRecommendations}>Get Recommendations</button>
      
      <h2>Recommendations</h2>
      <ul>
        {recommendations.map((product) => (
          <li key={product.id}>
            {product.name} (Similarity: {product.similarity_score.toFixed(2)})
            <button onClick={() => getProductInfo(product.id)}>More Info</button>
            <p>Recent Sales: {product.sales_data.reduce((sum, day) => sum + day.units_sold, 0)} units (Last 30 days)</p>
          </li>
        ))}
      </ul>

      {productInfo && (
        <div>
          <h2>Augmented Product Information</h2>
          <pre>{productInfo}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
