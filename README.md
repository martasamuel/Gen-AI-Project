# Retrieval Augmented Generation (RAG) Challenge

A RAG-Powered Exploration of Schizophrenia Literature Using OpenAI
Introduction

Retrieval Augmented Generation (RAG) is a powerful technique that combines retrieval-based and generation-based models to deliver accurate, context-aware responses. By integrating a vector database to fetch relevant documents and a large language model (LLM) to generate coherent outputs, RAG enhances the intelligence and relevance of generative AI systems across domains like healthcare, education, and research.

In this project, I applied the RAG architecture to a book focused on schizophrenia, leveraging OpenAI's LLMs to generate insightful and contextually rich responses based on retrieved content. This approach enables a more informed, nuanced understanding of complex mental health topics.

Project Overview

This project provides hands-on experience building a RAG system from scratch. The pipeline spans from data ingestion and embedding to retrieval and final response generation — culminating in a powerful, interactive tool for knowledge extraction.

1. Dataset Selection
Primary Dataset:

A comprehensive book on schizophrenia, containing medical, psychological, and social perspectives.
Why this dataset?
Schizophrenia is a multifaceted mental health condition. Building a RAG system on this topic can support educational tools, mental health support platforms, and scholarly research assistants.

2. Exploratory Data Analysis (EDA)
Performed an in-depth EDA to:

Understand document structure (chapters, sections, references)
Identify key terminology and recurring themes (e.g., symptoms, treatments, case studies)
Plan optimal chunking strategy for embedding and retrieval
Findings revealed the importance of domain-specific language, which informed the decision to use high-quality embeddings and precise chunking.

3. Embedding and Storing Chunks
3.A Embedding Documents

Transformed text chunks into vector embeddings
Embedding Model Used: text-embedding-ada-002 from OpenAI
Considered cost-efficiency and accuracy for medical-language content
3.B Connecting to Vector Database

Tool Used: ChromaDB for local storage and retrieval
Process:
Preprocessed book into semantically meaningful chunks
Generated embeddings with OpenAI
Stored in ChromaDB
Implemented retrieval based on semantic similarity


3.C AI Frameworks

Framework Used: LangChain 
Benefits: Simplified integration between components and accelerated development

4. Connecting to LLM
   
Objective:
Connect to a Large Language Model to generate responses based on contextually retrieved chunks.

LLM Used: OpenAI GPT (via openai API)
Combined user queries with retrieved content from ChromaDB
Engineered prompts to preserve context and tone appropriate for mental health topics

5. Evaluation
Manual Evaluation:

Created a set of mental health-related queries
Assessed the RAG system’s ability to extract relevant knowledge and provide meaningful answers

6. Deployment 
While full deployment wasn't the primary goal, a prototype web interface was explored using:

Frontend: Streamlit 
Future Work: Deploy via containerized services (e.g., Docker + Azure App Service)
