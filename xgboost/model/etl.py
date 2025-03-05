import pandas as pd
import requests
from dataclasses import dataclass, field

@dataclass
class BaseRequest:
    """base request for this API"""

    base_url="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Building_Permit_Applications_Feature_Layer_view/FeatureServer/0/query"
    params:dict = field(init=True, default_factory=lambda : {"outFields":"*", "where": "1=1","f":"json"})

    # post-initalized data
    data: pd.DataFrame = field(init=False)

    def __post_init__(self): 
        """post initialized build of data"""
        self.data = self.request()

    def request(self) -> pd.DataFrame: 
        """make request of class"""
        response = requests.get(self.base_url, params=self.params)

        if not response.status_code == 200: 
            raise ValueError(f"{response.reason}")

        request_json = response.json()
        data=pd.json_normalize(
            request_json,
            record_path=["features"]
        )
        
        data.columns = data.columns.str.replace("attributes.","")\
            .str.lower()\
            .str.removesuffix("__")\
            .str.replace(".","_")
        
        return data

@dataclass
class PermitsApplied(BaseRequest): 
    """permits applied for"""
    base_url="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Building_Permit_Applications_Feature_Layer_view/FeatureServer/0/query"

@dataclass
class PermitsIssued(BaseRequest): 
    """permits applied for"""
    base_url="https://services2.arcgis.com/HdTo6HJqh92wn4D8/arcgis/rest/services/Building_Permits_Issued_2/FeatureServer/0/query"
