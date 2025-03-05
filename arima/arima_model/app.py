from flask import Flask

def create_app(): 
    """create base application for Flask routes"""
    app = Flask(__name__)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()