
# Automotive Multimodal RAG System with FastAPI

## Problem Statement
Automotive technicians frequently rely on lengthy service manuals that contain
a mix of text explanations, diagnostic tables, and engineering diagrams.
Finding precise information in these documents is difficult because traditional
keyword search tools cannot understand context or relationships between
different parts of the document.

This project proposes a Multimodal Retrieval-Augmented Generation (RAG) system
to assist technicians in querying automotive service manuals. The system
ingests PDF manuals containing text, tables, and diagrams. It extracts and
processes these elements separately, converts them into embeddings, and stores
them in a vector database. When a user asks a question, the system retrieves the
most relevant chunks from the indexed documents and sends them to a language
model to generate a grounded response.

Such a system is useful in automotive workshops where technicians need quick
answers to diagnostic questions. Instead of manually scanning hundreds of pages
of documentation, they can ask natural language questions like:
- “What causes turbocharger overboost?”
- “Which sensor is responsible for intake pressure?”
- “What are the torque specifications in the engine table?”

The system therefore improves efficiency, reduces diagnostic time, and helps
technicians make informed repair decisions.

## Architecture Overview
User Query → Embedding → Vector Search → Context Builder → LLM → Final Answer

## Technology Choices
FastAPI – REST API server  
ChromaDB – Vector database  
SentenceTransformers – Embedding model  
PyPDF – Document parsing  
OpenRouter – LLM access

## Setup Instructions
1. Install dependencies

pip install -r requirements.txt

2. Run server

uvicorn main:app --reload

3. Open Swagger

http://localhost:8000/docs

## API Endpoints

GET /health – System status  
POST /ingest – Upload a PDF and index it  
POST /query – Ask questions from indexed documents  

## Limitations
Image summarization currently uses a placeholder approach.

## Future Work
Integrate a stronger vision-language model and improve table extraction.
