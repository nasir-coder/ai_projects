# Chatbot with ChatGPT and Web Scraping

<div align="center">
  <img src="https://cdn.pixabay.com/photo/2023/02/05/20/01/ai-generated-7770474_1280.png" alt="Chatbot Logo">
</div>

---

## 🚀 Overview

This project showcases the creation of an interactive chatbot using the ChatGPT API, seamlessly integrated with web scraping to extract information from a specified website. The chatbot interacts through both the console and a simple Flask API.

## 🛠️ Setup

### 1. Environment Setup

- Acquire the necessary API key for ChatGPT and store it in a `.env` file:

  ```plaintext
  OPENAI_API_KEY=<Your_OpenAI_API_Key>
##  Install required libraries:
- pip install Flask requests beautifulsoup4 python-dotenv openai

## 2. Extracting Data
The script leverages Beautiful Soup for HTML parsing to extract relevant information from the provided website.

## 3. Processing Data
Extracted data is structured and utilized as input to the ChatGPT API for generating meaningful responses.

## 4. Implementing the Chatbot
The chatbot is built using the ChatGPT API and designed to take user inputs, process them, and generate suitable responses.

## 5. Console Demonstration
The chatbot functions seamlessly via the console, allowing users to interact, ask questions, and receive relevant responses.

## 🚀 Usage
Console Interaction
i. Run the script:
-   bash
-   python chatbot.py
ii. The chatbot will prompt you to ask questions or provide input.

## Flask API
i. Run the Flask app:

-   bash
-   python chatbot.py
ii.Use the /ask endpoint to interact with the chatbot via HTTP POST requests.

## Example:

-   bash
-   curl -X POST -H "Content-Type: application/json" -d '{"user_input": "Tell me about the website"}' http://localhost:5000/ask
