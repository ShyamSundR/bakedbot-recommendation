from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from datapro import data_processor

class RecommendationSystem:
    def __init__(self):
        self.data_processor = data_processor

    def get_recommendations(self, preferences, top_n=5):
        # Convert preferences to embedding
        pref_embedding = data_processor.sentence_model.encode([preferences])[0]
        
        # Calculate cosine similarity
        similarities = cosine_similarity([pref_embedding], data_processor.embeddings)[0]
        
        # Prepare recommendations with type conversion
        recommendations = []
        for idx in sorted(
            range(len(similarities)), 
            key=lambda i: similarities[i], 
            reverse=True
        )[:top_n]:
            product = data_processor.products.iloc[idx]
            recommendations.append({
                'id': int(product['id']),
                'name': str(product['name']),
                'description': str(product['description']),
                'similarity_score': float(similarities[idx]),
                'price': float(product['price']),
                'sales_data': data_processor.get_product_sales(product['id'])
            })
        
        return recommendations

recommendation_system = RecommendationSystem()

