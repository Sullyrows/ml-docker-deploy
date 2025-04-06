import pathlib 
import joblib 
import pandas as pd
from dataclasses import dataclass, field
from statsmodels.tsa.arima.model import ARIMA, ARIMAResultsWrapper
from os import environ, getenv
from typing import Literal
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
        
    def predict(
        self, 
        data: pd.DataFrame | str, 
        data_format: Literal["csv", "pandas", "json"] = "pandas"
    ) -> pd.DataFrame | str:
        """predict using ARIMA model
        
        Args: 
            data (pd.DataFrame, str): data to predict on
            data_format (Literal["csv", "pandas", "json"]): format of data to return
        """
        if data.shape == (1,1) and "steps" in data.columns: 
            logger.info("Using steps for predictions of ARIMA")
            steps = int(data["steps"].values[0])
        else: 
            logger.info(f"Using data for predictions ({len(data.index)} rows)")
            steps = int(len(data.index))
        
        data = self.model.forecast(steps=steps)
        data.index.name = "date"
        
        if data_format == "csv": 
            data = data.to_csv(index=True) 
                   
        return data