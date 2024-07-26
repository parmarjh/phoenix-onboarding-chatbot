import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
import json

# Load the CSV file into a DataFrame
csv_file_path = 'C:/Users/ChatbotQuestionnaire.csv'  # Update with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Assuming the questions are in a column named 'question'
# Update the column name if it's different in your CSV
questions = df['Question'].tolist()

# Create and fit the tokenizer
tokenizer = Tokenizer(num_words=10000)  # Adjust num_words based on your needs
tokenizer.fit_on_texts(questions)

# Save the tokenizer to a JSON file
tokenizer_json = tokenizer.to_json()
with open('HR_AI_Chatbot_tokenizer.json', 'w', encoding='utf-8') as f:
    f.write(tokenizer_json)

print("Tokenizer has been created and saved successfully.")
