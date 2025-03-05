# app.py
from flask import Flask, request, jsonify
import numpy as np
from joblib import load
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load the model and scaler using joblib
model = load('model.joblib')
scaler = load('scaler.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get features from JSON request
        data = request.get_json()
        features = np.array(data['features']).reshape(1, -1)
        
        # Preprocess the features
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)
        
        return jsonify({
            'status': 'success',
            'prediction': prediction.tolist(),
            'prediction_probability': model.predict_proba(features_scaled).tolist()
        })
    
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy', 'model_version': '1.0'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)