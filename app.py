import os
import requests
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAI

load_dotenv()

SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")
GOOGLE_AI_API_URL = os.getenv("GOOGLE_API_KEY") 

def web_search(query):
    """Perform a web search using SerpAPI and return the results."""
    search_url = "https://serpapi.com/search"
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
    }
    
    response = requests.get(search_url, params=params)
    results = response.json()
    
    return results.get("organic_results", [])

def get_google_ai_answer(results):
    """Send search results to Google AI and return the answer."""
    prompt = "Based on the following search results, summarize the information:\n\n"
    for result in results:
        prompt += f"- Title: {result['title']}\n  Link: {result['link']}\n  Snippet: {result['snippet']}\n\n"
    prompt += "Provide the extact answer according to query latest result if query it is about stock then also provide two line discription and Key stock information."

  
    llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GOOGLE_AI_API_URL)
    answer = llm.generate([prompt])
    generated_text = answer.generations[0][0] if answer.generations and answer.generations[0] else "No answer generated."
    
    return generated_text

st.title("Web Searcher Using SerpAPI and Google AI")

search_query = st.text_input("Enter your search query:")

if st.button("Search"):
    if search_query:
        with st.spinner('Searching...'):
            results = web_search(search_query)
            
            if results:
                st.subheader("Answer from Google AI:")
                answer = get_google_ai_answer(results)
                st.write(answer.text)

                st.subheader("Search Results (Recent First):")
                for i, result in enumerate(results):
                   if i < 5:
                    st.markdown(f"**{i+1}. {result['title']}**")
                    st.write(result['snippet']) 
                    st.write(result['link'])  
            else:
                st.write("No results found.")
    else:
        st.error("Please enter a search query.")
