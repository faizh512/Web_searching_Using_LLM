# Web Searcher using SerpAPI and Google AI

This project implements a **web search tool** that integrates **SerpAPI** for web searches and **Google Generative AI** (Gemini Pro model) to summarize the search results. The tool is built using **Streamlit** for user interaction.

## Features

- **Web Search via SerpAPI**: Users can input a search query, and the app retrieves recent search results.
- **Google AI Summarization**: The search results are sent to Google Generative AI, which provides an accurate and concise summary.
- **Top Search Results Display**: Displays the top 5 search results, including title, snippet, and link.

## Prerequisites

To run this project, you'll need the following:

1. **Python 3.x** installed on your machine.
2. The following Python packages:
   - `os`
   - `requests`
   - `streamlit`
   - `dotenv`
   - `langchain_google_genai`

   Install them with the following command:

   ```bash
   pip install requests streamlit python-dotenv langchain_google_genai
