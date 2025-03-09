# AI-Powered Product Recommendation System

A prototype recommendation system with Retrieval-Augmented Generation (RAG) integration, built for the challenge.

## ✨ Features
- Hybrid recommendation engine (content-based + sales trends)
- RAG-enhanced product descriptions
- Simple REST API backend
- React-based user interface
- Mock dataset integration

## 🛠 Tech Stack
| Component       | Technologies Used               |
|-----------------|----------------------------------|
| Backend         | Node.js, Express, Python         |
| Frontend        | React, Axios                     |
| AI/ML           | Sentence Transformers, TF-IDF    |
| Data Storage    | JSON files                       |

## 🚀 Installation
1. Backend Setup
cd bakedbot-recommendation
npm install



2. Frontend Setup**
cd frontend
npm install


3. AI/ML Dependencies**
pip install -r mlrag/requirements.txt


📂 File Structure
.
├── data/ # Mock datasets
│ ├── products.json
│ ├── ingredients.json
│ └── sales.json
├── frontend/ # React application
├── mlrag/ # AI/ML components
│ ├── datapro.py # Data processing
│ ├── rag.py # RAG implementation
│ └── recommendationsys.py # Core algorithm
└── index.js # Node.js server


 🖥 Usage
Start Backend Server
node index.js


Start Frontend
cd frontend
npm start


Access the system at `http://localhost:xxxx'

🔧 Key Implementation Details
- Recommendation Algorithm 
  Combines TF-IDF vectorization with sentence transformers for semantic matching
- RAG Integration
  Enhances product info using ingredient data and sales history
- API Endpoints  
  - `GET /recommendations?preferences=...`  
  - `GET /product-info/:id`


## 🔮 Future Improvements
1. Add user preference history tracking
2. Integrate with LLM (e.g., GPT-3) for description generation
3. Implement collaborative filtering
4. Add authentication layer
5. Containerize using Docker

## ⚠️ Note
- Virtual environment (`venv`) excluded via .gitignore
- Python dependencies should be installed in virtual environment
