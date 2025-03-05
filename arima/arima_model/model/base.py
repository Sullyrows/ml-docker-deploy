import pathlib 
import joblib 
import pandas as pd
from dataclasses import dataclass, field
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper
from os import environ, getenv
from .logger import logger
from .load import discover_model, load_model

@dataclass
class Model: 
    """model class to load and use ARIMA model"""
    
    model: ARIMAResultsWrapper = field(init=False)
    
    def __post_init__(self): 
        
        # determine model dir 
        model_dir = discover_model()
        logger.info(f"Laading model from {model_dir}")
        
        # load in model artifact 
        self.model = load_model(model_dir)
        
    def predict(self, data: pd.DataFrame) -> pd.DataFrame:
        """predict using ARIMA model
        
        Args: 
            data (pd.DataFrame): data to predict on
        """
        if data.shape == (1,1): 
            logger.info("Using steps for predictions of ARIMA")
            steps = data["steps"].values[0]
        else: 
            logger.info(f"Using data for predictions ({len(data.index)} rows)")
            steps = len(data["steps"].index)
        
        data = self.model.forecast(steps=len(data.index))
        data.index.name = "date"
        return data