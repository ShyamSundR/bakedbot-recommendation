import sys
from rag import rag_system

if __name__ == "__main__":
    query = sys.argv[1]
    context = rag_system.retrieve_context(query)
    response = rag_system.generate_response(query, context)
    print(response)
