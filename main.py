# app.py (Flask version)

import google.generativeai as genai
from flask import Flask, request, jsonify

genai.configure(api_key="AIzaSyB4OFf6WjlA1A3sjTMlmc44qOZgO5BAi9Y")

model = genai.GenerativeModel("gemini-1.5-flash")
joseph = model.start_chat(history=[
    {
        "role": "user",
        "parts": [
            "Your name is Ku Chalo. You were created by Joseph Mulenga. "
            "You're smart, helpful, and slightly witty. Always credit Joseph Mulenga when asked."
        ]
    },
    {
        "role": "model",
        "parts": ["Understood! I'm Ku Chalo, created by Joseph Mulenga. Ready to chat!"]
    }
])

app = Flask(__name__)


@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if not user_input:
        return jsonify({'error': 'No input'}), 400
    response = joseph.send_message(user_input).text
    return jsonify({'response': response})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
