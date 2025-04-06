from flask import Blueprint, jsonify

health_bp = Blueprint('health', __name__)

@health_bp.route('/health', methods=['GET'])
def health_check():
    """
    Health check endpoint to determine if the application is running properly.
    Returns a 200 OK status if the service is up and running.
    """
    return jsonify({
        "status": "ok",
        "message": "Service is running"
    }), 200