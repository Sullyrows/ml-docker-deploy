import pytest
import pathlib
from flask import Flask
from flask.testing import FlaskClient
from arima_model.app import create_app

"""
Pytest configuration file for Flask application tests.
"""

# data directory
data_dir = pathlib.Path.cwd() / "arima/tests/data"

@pytest.fixture
def app():
    """Create and configure a Flask app for testing."""
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SM_MODEL_DIR": str(data_dir / "arima_model.joblib")
    })
    yield app


@pytest.fixture
def client(app):
    """Create a test client for the app."""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create a test CLI runner for the app."""
    return app.test_cli_runner()