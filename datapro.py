import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sentence_transformers import SentenceTransformer

class DataProcessor:
    def __init__(self):
        # Load data with explicit type conversion
        self.products = pd.read_json('/Users/shyamsunder/bakedbot-recommendation/data/products.json', dtype={
            'id': int,
            'price': float,
            'sales_data': dict
        })
        self.vectorizer = TfidfVectorizer()
        self.sentence_model = SentenceTransformer('all-MiniLM-L6-v2')
        self.ingredients = pd.read_json('/Users/shyamsunder/bakedbot-recommendation/data/ingredients.json')

    def get_ingredient_info(self, ingredient_name):
        ingredient = self.ingredients[self.ingredients['name'] == ingredient_name]
        return ingredient.iloc[0].to_dict() if not ingredient.empty else {}

    def preprocess_data(self):
        # Combine relevant text features
        self.products['text_features'] = self.products.apply(
            lambda x: f"{x['description']} {' '.join(x['effects'])}", axis=1
        )
        
        # Create TF-IDF vectors
        self.tfidf_matrix = self.vectorizer.fit_transform(self.products['text_features'])
        
        # Create sentence embeddings
        self.embeddings = self.sentence_model.encode(self.products['text_features'].tolist())

    def get_product_sales(self, product_id):
        # Load sales data from separate file
        sales_data = pd.read_json('/Users/shyamsunder/bakedbot-recommendation/data/sales.json')
        product_sales = sales_data[sales_data['product_id'] == product_id]
        
        if not product_sales.empty:
            return product_sales['daily_sales'].iloc[0]  # Return array of daily sales
        return []
data_processor = DataProcessor()
data_processor.preprocess_data()