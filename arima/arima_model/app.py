from flask import Flask
from arima_model.routes.health import health_bp


# register blueprints from routes

def create_app(): 
    """create base application for Flask routes"""
    app = Flask(__name__)
    app.register_blueprint(health_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()