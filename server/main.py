from flask import Flask, jsonify, request
import requests
from bs4 import BeautifulSoup

from flask_cors import CORS

app = Flask(__name__)
CORS(app) # to allow cross origin requests from react app

LLM_URL = "http://localhost:11434/api/generate"
header = {
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
    ollam
    return jsonify(
        {"url": url}
    )


if __name__ == "__main__":
    app.run(debug=True, port=8080)