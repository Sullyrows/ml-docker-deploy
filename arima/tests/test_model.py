"""tests for model classes and loading"""
import pytest 
import pathlib
from arima_model.model.load import load_model, discover_model
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper

data_dir = pathlib.Path.cwd() / "arima/tests/data"

def test_load_model():
    """test execution of load_model function"""
    # load arima model 
    arima_model = load_model(data_dir / "arima_model.joblib")
    
    assert isinstance(arima_model, ARIMAResultsWrapper)
    

def test_model_discovery(monkeypatch): 
    """test that environment variables can read to paths"""
    
    # set environment variable 
    monkeypatch.setenv("SM_MODEL_DIR", str(data_dir / "arima_model.joblib"))
    
    model_path = discover_model()
    assert str(model_path) is not None
    assert model_path.exists()