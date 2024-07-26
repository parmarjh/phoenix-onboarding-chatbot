from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import json
import re
import pandas as pd
from difflib import get_close_matches

app = Flask(__name__)

# Load pre-trained TensorFlow model
model = tf.keras.models.load_model('../HR_Chatbot_trained_model.h5')

# Load the tokenizer
with open('../HR_AI_Chatbot_tokenizer.json', 'r', encoding='utf-8') as f:
    tokenizer_config = json.load(f)
tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(json.dumps(tokenizer_config))

# Load the CSV data
data = pd.read_csv('../ChatbotQuestionnaire.csv')

# Preprocess text
def preprocess_text(text):
    return text.lower()

# Preprocess the data
data['Question'] = data['Question'].apply(preprocess_text)
categories = data['Category'].astype('category').cat.categories.tolist()

# Max length for padding
max_len = 100

# Static answers dictionary
static_answers = {
    "time off": "To request time off, please submit a leave request form through the employee portal.",
"leave policy": "Our company offers various types of leave including annual leave, sick leave, and parental leave.",
"leave": "Our company offers various types of leave including annual leave, sick leave, and parental leave.",
"employment verification": "To request an employment verification letter, please contact HR with your request.",
"verification": "To request an employment verification letter, please contact HR with your request.",
"employment": "To request an employment verification letter, please contact HR with your request.",
"it support": "For IT support, please contact the IT helpdesk via email at support@company.com.",
"support": "For IT support, please contact the IT helpdesk via email at support@company.com.",
"it": "For IT support, please contact the IT helpdesk via email at support@company.com.",
"personal information": "To update your personal information, please visit the employee portal and navigate to "
                        "the personal details section",
"performance review": "Performance reviews are conducted annually. Please check with HR for specific dates and "
                      "procedures.",
"performance": "Performance reviews are conducted annually. Please check with HR for specific dates and procedures.",
"review": "Performance reviews are conducted annually. Please check with HR for specific dates and procedures.",
"pay stubs": "You can access your pay stubs through the payroll section of the employee portal.",
"payroll": "You can access your pay stubs through the payroll section of the employee portal.",
"salary slip": "You can access your pay stubs through the payroll section of the employee portal.",
"pay slip": "You can access your pay stubs through the payroll section of the employee portal.",
"salary certificate": "You can access your pay stubs through the payroll section of the employee portal.",
"salary": "You can access your pay stubs through the payroll section of the employee portal.",
"remote work": "Our company allows remote work.Talk to your Line Manager for more information.",
"remote": "Our company allows remote work.Talk to your Line Manager for more information.",
"wfh": "Our company allows remote work.Talk to your Line Manager for more information.",
"work from home": "Our company allows remote work.Talk to your Line Manager for more information.",
"remote access": "Our company allows remote work.Talk to your Line Manager for more information",
"workplace harassment": "Report any incidents of workplace harassment to HR immediately.You can do so via email or in person",
"harassment": "Report any incidents of workplace harassment to HR immediately.You can do so via email or in person.",
"posh": "Report any incidents of workplace harassment to HR immediately. You can do so via email or in person.",
"benefits": "Our company offers health insurance, retirement plans, and various employee perks."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message']
    response = generate_response(user_message)
    return jsonify(response)

def generate_response(user_message):
    # Preprocess the user message
    processed_message = preprocess_text(user_message)

    # Handle greetings with regular expressions
    greetings_pattern = re.compile(r'\b(hi|hey|hello)\b', re.IGNORECASE)
    if greetings_pattern.search(processed_message):
        return {'response': 'Hello! How may I help you?'}

    # Split the user message into words
    user_words = set(processed_message.split())

    # Check for static answers based on keywords
    for keyword, response in static_answers.items():
        if any(get_close_matches(word, [keyword], n=1, cutoff=0.8) for word in user_words):
            return {'response': response}

    # Initialize variables to find the best match
    best_match_score = 0
    best_response = "Please contact helpdesk in-person for clarification."

    # Iterate through each question in the dataset
    for index, row in data.iterrows():
        question_words = set(preprocess_text(row['Question']).split())
        common_words = user_words.intersection(question_words)
        match_score = len(common_words)  # Score based on common words

        # Check if this question has a higher match score
        if match_score > best_match_score:
            best_match_score = match_score
            best_response = row['Response']

    return {'response': best_response}

if __name__ == "__main__":
    app.run(debug=True)
