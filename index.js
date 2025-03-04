const express = require('express');
const app = express();
const products = require('./data/products.json');
const ingredients = require('./data/ingredients.json');
const cors = require('cors');
app.use(cors());

app.use(express.json()); // Middleware to parse JSON requests

// Start server on port 3000
app.listen(3000, () => console.log('Backend running on http://localhost:3000'));


//Recommendation
app.get('/recommendations', (req, res) => {
    const userPreferences = req.query.preferences ? req.query.preferences.split(',') : [];
    
    // Filter products based on user preferences (e.g., "relaxation")
    const recommendedProducts = products.filter(product =>
        userPreferences.some(pref => product.effects.includes(pref))
    );

    res.json(recommendedProducts);
});


//Product info
app.get('/product-info/:id', (req, res) => {
    const productId = parseInt(req.params.id);
    const product = products.find(p => p.id === productId);

    if (!product) {
        return res.status(404).send('Product not found');
    }

    // Augment product information with ingredient properties
    const augmentedIngredients = product.ingredients.map(ingredientName => {
        const ingredientDetails = ingredients.find(i => i.name === ingredientName);
        return {
            name: ingredientName,
            properties: ingredientDetails ? ingredientDetails.properties : 'No details available'
        };
    });

    const augmentedProduct = {
        ...product,
        augmentedIngredients,
    };

    res.json(augmentedProduct);
});

