import pathlib 
import joblib
import pandas as pd 
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper
from os import environ, getenv
from .logger import logger


def load_model(model_path: str) -> pd.DataFrame:
    """load model from path 
    
    Args: 
        model_path (str, pathlib.Path): the path to the model artifacts to laod in.
    """
    
    
        