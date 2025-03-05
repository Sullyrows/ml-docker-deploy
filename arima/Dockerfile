FROM python:3.12-slim

WORKDIR /opt/ml/code

COPY arima_model/ /opt/ml/code/arima_model/

# If you have requirements, you can uncomment and use these lines
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Set Python path to include the model directory
ENV PYTHONPATH=/opt/ml/code:$PYTHONPATH

# Default command when container starts
CMD ["python"]