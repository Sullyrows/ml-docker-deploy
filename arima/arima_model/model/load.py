import pathlib 
import joblib
import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper
from os import environ, getenv
from .logger import logger

def discover_model() -> pathlib.Path:
    """discover joblib file from environment variable, SM_MODEL_DIR
    
    Returns: 
        model_path (pathlib.Path): path to model file 
    """
    
    if not getenv("SM_MODEL_DIR"): 
        logger.info("Loading model from default - /opt/ml/model")
    
    # determine inbound model path 
    sm_model= pathlib.Path(getenv("SM_MODEL_DIR", "/opt/ml/model"))
    
    if sm_model.is_dir(): 
        logger.debug("model path is a directory, using first joblib file")

        # get the first joblib file in the directory
        model_path = next(sm_model.glob("*.joblib"), None)
        
        if model_path is None:
            raise FileNotFoundError(f"No joblib file found in {sm_model}")
    else:
        model_path = sm_model
        
    return model_path


def load_model(model_path: str | pathlib.Path) -> object:
    """load model artifactcs from model_path
    
    Args: 
        model_path (str, pathlib.Path): path to model file 
    """
    return joblib.load(model_path)