from sentence_transformers import util
from datapro import data_processor

class RAGSystem:
    def __init__(self):
        self.data_processor = data_processor

    def retrieve_context(self, query, top_k=3):
        query_embedding = self.data_processor.sentence_model.encode([query])[0]
        
        # Calculate cosine similarity
        similarities = util.cos_sim([query_embedding], self.data_processor.embeddings)[0]
        
        # Get top K similar products
        top_indices = similarities.argsort()[-top_k:][::-1]
        
        context = []
        for idx in top_indices:
            product = self.data_processor.products.iloc[idx]
            ingredients = self.data_processor.ingredients[self.data_processor.ingredients['name'].isin(product['ingredients'])]
            context.append({
                'product_name': product['name'],
                'product_description': product['description'],
                'ingredients': ingredients.to_dict('records')
            })
        
        return context

    def generate_response(self, query, context):
        # In a real-world scenario, you would use an LLM here.
        # For this prototype, we'll just combine the context into a response.
        response = f"Based on your query '{query}', here's some relevant information:\n\n"
        for item in context:
            response += f"Product: {item['product_name']}\n"
            response += f"Description: {item['product_description']}\n"
            response += "Ingredients:\n"
            for ing in item['ingredients']:
                response += f"- {ing['name']}: {ing['properties']}\n"
            response += "\n"
        return response

rag_system = RAGSystem()
