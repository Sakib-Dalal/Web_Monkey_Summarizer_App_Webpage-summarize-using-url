# Web Monkey Summarizer

<hr>
<img src="./screenshots/img 2.png">
<br>
<hr>

Web Monkey Summarizer is a full-stack application that allows users to summarize web pages easily. Copy the URL of the webpage you want to summarize, paste it into the input box, click “Submit,” and get a concise summary of the content.

Features
	•	Easy-to-use interface: Copy, paste, and summarize in seconds.
	•	Powered by AI: Uses the Ollama 3.2 LLM for generating accurate and meaningful summaries.
	•	Full-stack architecture: Combines the power of React.js on the frontend with Flask and Ollama on the backend.

Technologies Used

Frontend
	•	React.js
	•	Vite
	•	Axios

Backend
	•	Python Flask
	•	Ollama 3.2 (1-billion parameter model)
	•	Requests library

How to Run Locally

Prerequisites
	•	Node.js and npm
	•	Python 3.7+
	•	Flask
	•	Ollama installed locally

Steps

1.	Clone the repository:
git clone https://github.com/Sakib-Dalal/Website-Summariser.git
cd Website-Summariser


2.	Setup the Backend:
    •	Navigate to the backend directory:
    `cd server`

    • Install the required Python packages:
    `pip install -r requirements.txt`

    • Run the Flask server:
    `python app.py`


3.	Setup the Frontend:
    •	Navigate to the frontend directory:
    `cd client`

    • Install dependencies:
    `npm install`

    • Start the React application:
    `npm run dev`

4.	Open the application in your browser. By default, the frontend runs on http://localhost:5173, and the backend runs on http://localhost:8080.

Deployment

For deployment, you can use platforms like:
	•	Frontend: Vercel, Netlify
	•	Backend: AWS EC2, Heroku, or any Flask-compatible hosting.

Contribution

Contributions are welcome! Fork the repository, create a branch, and submit a pull request. Ensure your changes are well-documented.

