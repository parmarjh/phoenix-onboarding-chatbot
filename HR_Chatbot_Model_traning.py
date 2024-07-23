import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pandas as pd
from sklearn.model_selection import train_test_split

# Load dataset
data = pd.read_csv(r'C:/Users/ChatbotQuestionnaire.csv')

# Preprocess text
def preprocess_text(text):
    text = text.lower()
    return text

data['Question'] = data['Question'].apply(preprocess_text)

# Split data
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Tokenize the questions
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(train_data['Question'])

# Convert text to sequences
train_sequences = tokenizer.texts_to_sequences(train_data['Question'])
test_sequences = tokenizer.texts_to_sequences(test_data['Question'])

# Pad sequences
max_length = 100
train_padded = pad_sequences(train_sequences, maxlen=max_length, padding='post')
test_padded = pad_sequences(test_sequences, maxlen=max_length, padding='post')

# Define model
model = Sequential([
    Embedding(input_dim=5000, output_dim=64, input_length=max_length),
    LSTM(64, return_sequences=True),
    LSTM(64),
    Dense(32, activation='relu'),
    Dense(len(data['Category'].unique()), activation='softmax')
])

# Compile model
model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model
train_labels = train_data['Category'].astype('category').cat.codes
test_labels = test_data['Category'].astype('category').cat.codes

model.fit(train_padded, train_labels, epochs=10, validation_data=(test_padded, test_labels))

# Save the model
model.save('HR_Chatbot_trained_model.h5')
