from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import openai
import os
from dotenv import load_dotenv

# Loading environment variables from .env file
load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)

def extract_data_from_website(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    website_data = {
        "title": soup.title.text if soup.title else "No title available",
        "description": soup.find("meta", property="og:description")["content"] if soup.find("meta", property="og:description") else "No description available",
    }
    return website_data

def generate_response(user_input, extracted_data):
    if extracted_data is not None:
        input_data = f"Website data: {extracted_data['title']}\nDescription: {extracted_data['description']}\nUser input: {user_input}"

        try:
            print("Calling OpenAI API with input:")
            print(input_data)

            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=input_data,
                max_tokens=100,
                temperature=0.7,
            )

            print("Response from OpenAI API:")
            print(response)

            return response.choices[0].text.strip()
        except Exception as e:
            print(f"Error calling OpenAI API: {e}")
            return "An error occurred while generating a response"
    else:
        return "No data available"

url = "https://botpenguin.com/"
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    html_content = response.text
else:
    print(f"Failed to retrieve the content. Status code: {response.status_code}")
    exit()

print("Chatbot: Hello! I am a chatbot. You can ask me anything about the website.")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    extracted_data = extract_data_from_website(html_content)
    print(f"Extracted Data: {extracted_data}")

    response = generate_response(user_input, extracted_data)
    print(f"Chatbot: {response}")

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    user_input = data['user_input']

    extracted_data = extract_data_from_website(html_content)
    response = generate_response(user_input, extracted_data)

    return jsonify({'response': response})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)