from tensorflow.keras.preprocessing.text import Tokenizer
import json

# Example texts used for training the tokenizer
texts = [
    "What are the types of reimbursements I can claim?",
    "What is the process of claiming reimbursements?",
    "Where to declare investments?",
    "How to select Tax Regime for current Financial Year?",
    "How to claim medical insurance?",
    "What are the various types of leave options available for employees?",
    "How do I apply for leave?",
    "How can I view my annual leave balance?",
    "What is the policy for sick leave?",
    "What is the policy for emergency leaves?",
    "How many weeks of maternity/paternity leave am I entitled to?",
    "What are the working hours for the company?",
    "What is the company's work from home policy?",
    "How do I fill out the Clarity time sheet?",
    "What is the policy on flexible working hours?",
    "Where can I find the leave/attendance/WFH policy document?",
    "Who do I reach out to for further clarifications?",
    "Do the company provide transport facility?",
    "Do the company provide meals?",
    "Are there any committees for employee engagement?"
]

# Create and fit the tokenizer
tokenizer = Tokenizer(num_words=10000)  # Adjust num_words
tokenizer.fit_on_texts(texts)

# Save the tokenizer
tokenizer_json = tokenizer.to_json()
with open('HR_AI_Chatbot_tokenizer.json', 'w') as f:
    f.write(tokenizer_json)
