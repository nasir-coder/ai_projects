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
###  Install required libraries:
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

### Console Interaction

```bash
# Run the Script
python chatbot.py
