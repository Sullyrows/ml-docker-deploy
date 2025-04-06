import pytest 
import pandas as pd 
import pathlib
from arima_model.model.base import Model
from io import StringIO

@pytest.fixture
def my_model(monkeypatch) -> Model: 
    """model fixture for testing model class building"""
    monkeypatch.setenv("SM_MODEL_DIR", pathlib.Path.cwd() / "arima/tests/data/arima_model.joblib")
    return Model()

class Test_Model: 
    """test model class attributes"""
    
    data_sets = [
        pd.DataFrame({"steps": [3]}),
        pd.DataFrame({"sales": [22200, 22400, 22600]})
    ]
    
    def test_model_exists(self, my_model: Model): 
        """test that model exists"""
        assert my_model.model is not None
        
    @pytest.mark.parametrize("payload", data_sets)
    def test_predict_csv(self, payload: pd.DataFrame, my_model: Model): 
        """test predict method with csv output"""
        # test that model can predict
        predictions = my_model.predict(payload, data_format="csv")
        
        # assert that prediction can be readable 
        pred_df = pd.read_csv(StringIO(predictions))
        assert isinstance(pred_df, pd.DataFrame)
        assert isinstance(predictions, str)
        
        
        