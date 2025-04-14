import streamlit as st
import openai
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
import os


@st.cache_resource
def load_chromadb():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    return db
db = load_chromadb()

api_key = os.getenv("OPENAI_API_KEY")


# Streamlit UI
st.title("🔬 Schizophrenia & Serotonin Research Assistant")

# User question input
user_question = st.text_input("🔍 Ask a question related to Schizophrenia and Serotonin:")

def _get_document_prompt(docs):
    """Formats retrieved documents into a context string."""
    prompt = "\n"
    for doc in docs:
        prompt += f"\nContent:\n{doc.page_content}\n\n"
    return prompt

if st.button("Get Answer") and user_question:
    # Retrieve relevant documents
    retrieved_docs = db.similarity_search(user_question, k=10)
    st.write(f"🔎 Retrieved {len(retrieved_docs)} relevant documents.")

    # Format context for the model
    formatted_context = _get_document_prompt(retrieved_docs)

    # Construct the final prompt
    prompt = f"""
    ## SYSTEM ROLE
    You are a knowledgeable and factual chatbot designed to assist with technical questions about **Schizophrenia**, specifically focusing on **Serotonin Relation**. 
    Your answers must be based exclusively on provided content from the technical book.

    ## USER QUESTION
    The user has asked: "{user_question}"

    ## CONTEXT
    Here is the relevant content from the technical book:  
    '''
    {formatted_context}
    '''

    ## GUIDELINES
    1. **Accuracy**:  

   - Only use the content in the `CONTEXT` section to answer.  
   - If the answer cannot be found, explicitly statestr: "The provided context does not contain this information."
   - Start explaining the relevance of the question in the context of this book

    ## RESPONSE FORMAT
    '''
    # [Brief Title of the Answer]
    [Answer in simple, clear text.]

    **Source**:  
    • [Book Title], Page(s): [...]
    '''
    """

    # OpenAI API call
    client = openai.OpenAI()
    model_params = {
        'model': 'gpt-4o',
        'temperature': 0.7,
        'max_tokens': 4000,
        'top_p': 0.9,
        'frequency_penalty': 0.5,
        'presence_penalty': 0.6
    }

    messages = [{'role': 'user', 'content': prompt}]
    completion = client.chat.completions.create(messages=messages, **model_params, timeout=120)

    # Get response
    answer = completion.choices[0].message.content
    st.markdown("### 🧠 AI Response")
    st.markdown(answer)