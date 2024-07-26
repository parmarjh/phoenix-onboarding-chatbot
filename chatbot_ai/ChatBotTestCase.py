import unittest
from app import app, preprocess_text, static_answers, generate_response
import json
import pandas as pd

class ChatbotTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_static_answers(self):
        test_cases = [
            ('time off', static_answers['time off']),
            ('leave policy', static_answers['leave policy']),
            ('employment verification', static_answers['employment verification']),
            ('it support', static_answers['it support']),
            ('personal information', static_answers['personal information']),
            ('performance review', static_answers['performance review']),
            ('pay stubs', static_answers['pay stubs']),
            ('remote work', static_answers['remote work']),
            ('workplace harassment', static_answers['workplace harassment']),
            ('benefits', static_answers['benefits']),
        ]
        for user_input, expected_response in test_cases:
            response = self.app.post('/get_response', data={'message': user_input})
            data = json.loads(response.data)
            self.assertEqual(data['response'], expected_response)

    def test_greetings(self):
        greetings = ['hi', 'hello', 'hey']
        expected_response = 'Hello! How may I help you?'
        for greeting in greetings:
            response = self.app.post('/get_response', data={'message': greeting})
            data = json.loads(response.data)
            self.assertEqual(data['response'], expected_response)

    def test_dynamic_response(self):
        # Load the CSV data and select a test question and its response
        data = pd.read_csv('../ChatbotQuestionnaire.csv')
        test_question = data['Question'].iloc[0]
        expected_response = data['Response'].iloc[0]

        # Test dynamic response generation
        response = self.app.post('/get_response', data={'message': test_question})
        data = json.loads(response.data)
        self.assertEqual(data['response'], expected_response)

if __name__ == '__main__':
    unittest.main()
