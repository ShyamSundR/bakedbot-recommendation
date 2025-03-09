const express = require('express');
const { spawn } = require('child_process');
const cors = require('cors');

const app = express();
app.use(cors());
app.use(express.json());

app.get('/recommendations', (req, res) => {
  const preferences = req.query.preferences;
  
  const python = spawn('python', ['mlrag/get_recommendations.py', preferences]);
  let dataString = '';

  python.stdout.on('data', (data) => {
    dataString += data.toString();
  });

  python.on('close', (code) => {
    console.log(`Python process exited with code ${code}`);
    res.json(JSON.parse(dataString));
  });
});

app.get('/product-info/:id', (req, res) => {
  const productId = req.params.id;
  const query = `Tell me about product ${productId}`;
  
  const python = spawn('python', ['mlrag/get_response.py', query]);
  let dataString = '';

  python.stdout.on('data', (data) => {
    dataString += data.toString();
  });

  python.on('close', (code) => {
  console.log(`Python process exited with code ${code}`);
  try {
      if (dataString.trim() === '') {
          throw new Error('Empty response from Python script');
      }
      const result = JSON.parse(dataString);
      res.json(result);
  } catch (e) {
      console.error('Failed to parse:', dataString);
      res.status(500).json({ 
          error: 'AI processing failed',
          details: e.message
      });
  }
  });
}); 

app.listen(3000, () => console.log('Server running on port 3000'));

