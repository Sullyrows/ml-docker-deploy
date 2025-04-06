import pandas as pd
from io import StringIO
from typing import Literal

def read_payload(
    payload: str, 
    content_type: Literal["application/json", "text/csv"] = "text/csv"
) -> pd.DataFrame: 
    """read in payload for the arima model"""
    
    # save payload to buffer 
    if content_type == "application/json": 
        data = pd.read_json(StringIO(payload))
    elif content_type == "text/csv":
        data = pd.read_csv(StringIO(payload))
    else: 
        raise NotImplementedError("Content type not supported")
    
    # conditional for simple "steps support"
    if data.shape == (1,1) and "steps" in data.columns: 
        return data
    
    # read in date and index data correctly 
    if not "date" in data.columns: 
        raise ValueError("Date column not found in data")
    
    data = data.set_index("date")
    # format index 
    data.index = pd.to_datetime(data.index)
    data.index = data.index.to_period("M")
    data.index.name = "date"
    
    return data