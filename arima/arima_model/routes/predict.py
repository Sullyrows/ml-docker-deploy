from flask import Blueprint, request, jsonify
import pandas as pd
import json
from arima_model.model.base import Model
from .logger import logger

predict_bp = Blueprint('predict', __name__)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    """
    Endpoint to serve predictions from the ARIMA model.
    
    Accepts:
        - JSON with 'steps' field for forecasting future steps
        - CSV data for prediction
        
    Returns:
        - JSON response with predictions or error message
    """
    
    try:
        # Initialize the model
        model = Model()
        
        # Check request content type
        if request.content_type == 'application/json':
            data = request.json
            
            # Handle steps-based prediction
            if 'steps' in data:
                steps = data['steps']
                input_df = pd.DataFrame({'steps': [steps]})
                output_format = data.get('output_format', 'json')
                
                # Get predictions
                if output_format.lower() == 'csv':
                    result = model.predict(input_df, data_format="csv")
                    return result, 200, {'Content-Type': 'text/csv'}
                else:
                    result = model.predict(input_df, data_format="pandas")
                    return jsonify({'predictions': json.loads(result.to_json())})
            
            return jsonify({'error': 'Invalid JSON input format. Must contain "steps" field.'}), 400
            
        # Handle CSV input
        elif request.content_type == 'text/csv':
            csv_data = request.data.decode('utf-8')
            input_df = pd.read_csv(pd.StringIO(csv_data))
            
            # Check for output format in query parameters
            output_format = request.args.get('output_format', 'json')
            
            # Get predictions
            if output_format.lower() == 'csv':
                result = model.predict(input_df, data_format="csv")
                return result, 200, {'Content-Type': 'text/csv'}
            else:
                result = model.predict(input_df, data_format="pandas")
                return jsonify({'predictions': json.loads(result.to_json())})
        
        else:
            return jsonify({'error': 'Unsupported content type. Use application/json or text/csv'}), 415
            
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        return jsonify({'error': str(e)}), 500