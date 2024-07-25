from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import json

app = Flask(__name__)

# Load pre-trained TensorFlow model
model = tf.keras.models.load_model('C:/Users/Sanghamitr Lahiri/HR_Chatbot_trained_model.h5')

# Load the tokenizer
with open('C:/Users/Sanghamitr Lahiri/HR_AI_Chatbot_tokenizer.json', 'r', encoding='utf-8') as f:
    tokenizer_config = json.load(f)
tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(json.dumps(tokenizer_config))

max_len = 20  # Assuming this is the maximum length of the input sequences


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
    sequences = tokenizer.texts_to_sequences([user_message])
    padded_sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_len, padding='post')

    # Get model prediction
    prediction = model.predict(padded_sequences)
    response_index = np.argmax(prediction)

    # Load responses
    responses = [
        "You can typically claim reimbursements for expenses like business travel, healthcare costs, education expenses, and mobile and internet bills.",
        "To claim reimbursements, collect all relevant receipts, fill out the reimbursement form <Portal Link> according to the type of expenses you want to claim, and submit the form with relevant details.",
        "To declare your investments, log into workday and click on Payroll. You will be redirected to Process Pay. On the Home Page, click on 'Submit Tax Declaration'. Fill out the necessary forms and submit the necessary documents. Here is the video link, for your guidance. <Video Link>",
        # more response adding
    ]

    # Check if the response index is valid
    if response_index < len(responses):
        response = responses[response_index]
    else:
        response = "Please contact helpdesk in-person for clarification."

    return {'response': response}


if __name__ == "__main__":
    app.run(debug=True)
