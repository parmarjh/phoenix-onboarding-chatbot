import google.auth
from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)

PROJECT_ID = 'lloyds-hack-grp-10'
REGION = 'us-central1'
ENDPOINT_ID = '3005622786665218048'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data
    data = request.json
    # Authenticate and initialize the AI Platform client
    credentials, project = google.auth.default()
    client_options = {"api_endpoint": f"us-central1-aiplatform.googleapis.com"}
    client = aiplatform.gapic.PredictionServiceClient(credentials=credentials, client_options=client_options)

    # Prepare the request
    endpoint = client.endpoint_path(project="lloyds-hack-grp-10", location="us-central1", endpoint="3005622786665218048")
    instances = data['instances']
    response = client.predict(endpoint=endpoint, instances=instances)

    # Return the prediction
    return jsonify(response.predictions)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)