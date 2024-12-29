from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup
import json

from flask_cors import CORS

app = Flask(__name__)
CORS(app) # to allow cross origin requests from react app

LLM_URL = "http://localhost:11434/api/generate"
headers = {
    "Content-Type": "application/json"
}

# # Web scraping
# url = "https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/"
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# # Extracting data
# data = {
#     "html_title": soup.text
# }

def llm_get(html_data):
    data = {
        "model": "llama3.2:1b",
        "prompt": f"given the html data summarize it. data: {html_data}. Note: Dont say that you are using web scraping in output, you can add your own information also. Give response in English Language.",
        "stream": False
    }
    try: 
        llm_res = requests.post(LLM_URL, headers=headers, data=json.dumps(data))
        llm_res.raise_for_status()
        return llm_res.json()
    except requests.exceptions.RequestException as e:
        print(f"Error connecting to LLM: {e}")
        return {"error": "Failed to connect to LLM service."}

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "OK",
    }), 200

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    url = data.get("url", "")
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, "html.parser")
    data = soup.text
    llm_output = llm_get(data)

    return jsonify(
        {"llm_res": llm_output["response"]}
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)