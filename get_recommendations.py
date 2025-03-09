import sys
import json
from recommendationsys import recommendation_system

try:
    preferences = sys.argv[1]
    recommendations = recommendation_system.get_recommendations(preferences)
    print(json.dumps(recommendations, indent=2))
except Exception as e:
    print(json.dumps({"error": str(e)}))
    sys.exit(1)
