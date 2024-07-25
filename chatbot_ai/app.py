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
        "To claim reimbursements, collect all relevant receipts, fill out the reimbursement form according to the type of expenses you want to claim, and submit the form with relevant details.",
        "To declare your investments, log into workday and click on Payroll. You will be redirected to Process Pay. On the Home Page, click on 'Submit Tax Declaration'. Fill out the necessary forms and submit the necessary documents. For more details contact HR department.",
        "To claim medical insurance, follow these steps: 1. Obtain medical bills and reports. 2. Fill out the insurance claim form. 3. Attach necessary documents. 4. Submit the form to the insurance provider. 5. Await approval and reimbursement.",
        "You have a variety of leave options including annual leave, sick leave, maternity leave, paternity leave, bereavement leave, personal leave, and study leave.",
        "Applying for leave is simple. You need to fill out the leave application form available on workday under 'My Absences'. Once completed, submit the form. Your Line Manager has to approve your leaves. Make sure to provide the necessary details such as the type of leave, dates, and any supporting documentation required (if applicable).",
        "To check your leave balance, you can log into workday and navigate to the 'My Balances' section. There, you will find your current leave balances displayed.",
        "Our company provides sick leave to ensure employees can recover from illness without worrying about work. You are entitled to 15 days of sick leave per year. A medical certificate may be required for absences longer than 5 days. For more details, please refer to the company's sick leave policy document.",
        "To apply for emergency leave, inform your Line Manager immediately about the situation. Ensure you provide necessary documentation if required. For more details, please refer to the employee handbook.",
        "Our company offers maternity or paternity leave of up to 12 weeks. Employees are required to apply on workday and provide a medical certificate",
        "The generic working hours are from 9 AM to 6 PM, Monday to Friday. This depends on the team you are in. For more details kindly discuss with your Line Manager.",
        "We follow a 3 days work from office and 2 days work from home in a week. To know more about your allotted days, kindly discuss with your line manager",
        "To fill out the Clarity time sheet, log in to the Clarity system, navigate to the 'Time Sheet' section, select the appropriate project and tasks, enter the hours worked for each day, and then save and submit your time sheet. If you need further assistance, refer to the user guide.",
        "Our company allows flexible working hours to accommodate employees' needs. You can discuss and arrange your schedule with your Line manager, ensuring that core working hours are maintained and work goals are met.",
        "You can find the leave policy document on the sharepoint home page.",
        "You can find the contact person for more details in the company directory on our sharepoint or by contacting the HR department",
        "Yes, our company provides a transport facility for employees. For more details on routes, timings, and how to avail this service, please refer to the transport policy on workday or contact the admin department.",
        "Yes, our company provides meals for employees. We offer lunch in the cafeteria. You can find the meal schedule and menu on the sharepoint.",
        "Yes, we have an Employee Engagement Committee like Sports, Music, Health and Safety committees dedicated to organizing activities and initiatives to keep employees motivated and connected. Find more in SharePoint."
    ]

    # Check if the response index is valid
    if response_index < len(responses):
        response = responses[response_index]
    else:
        response = "Please contact helpdesk in-person for clarification."

    return {'response': response}


if __name__ == "__main__":
    app.run(debug=True)
