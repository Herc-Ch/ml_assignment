from fastapi import FastAPI, HTTPException, Request
from typing import List
import pandas as pd
import os
import logging

# Create a logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Initialize logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# FileHandler for logging to a file
file_handler = logging.FileHandler("logs/app.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

app = FastAPI()

# Load the data
with open("cvas_data.json", "r") as fk:
    data = pd.read_json(fk)

# Feature Engineering function
def feature_engineering(data: pd.DataFrame) -> pd.DataFrame:
    data = pd.json_normalize(data['data'],record_path = ['loans'])
    # Your feature engineering code goes here
    # For example, you can create some new features based on existing ones
    data["loan_date"] = pd.to_datetime(data["loan_date"],dayfirst=True)
    data["year"] = data["loan_date"].dt.year
    # One can also apply dummy variables for the term column to be categorical for machine learning purposes (0 for long 1 for short)
    term_dummies = pd.get_dummies(data['term'], prefix='term', drop_first=True)
    data = pd.concat([data, term_dummies], axis=1)
    # And so on and so forth, eg. changing objects to int
    data[['amount','fee']] = data.apply(lambda row: row[['amount', 'fee']].astype(int), axis=1)
    # etc
    return data

# API endpoint for Feature Engineering
@app.get("/feature_engineering", response_model=List[dict])
async def perform_feature_engineering_get():
    logger.info("API endpoint for feature engineering (GET) called.")
    result = feature_engineering(data)
    # Convert boolean columns to integers
    bool_columns = result.select_dtypes(include='bool').columns
    result[bool_columns] = result[bool_columns].astype(int)
    logger.info("Feature engineering results returned.")
    return result.to_dict(orient="records")

@app.post("/feature_engineering", response_model=List[dict])
async def perform_feature_engineering_post(request: Request):
    logger.info("API endpoint for feature engineering (POST) called.")
    try:
            # Assuming the input data is sent as JSON in the request body
      
            data = await request.json()
       
          
            result = feature_engineering(data)
            
            # Convert boolean columns to integers
            bool_columns = result.select_dtypes(include='bool').columns
            result[bool_columns] = result[bool_columns].astype(int)
            
            # Convert the DataFrame to a list of dictionaries and return
            logger.info("Feature engineering results returned.")
            return result.to_dict(orient="records")
        
    except Exception as e:
            logger.error(f"API endpoint for feature engineering (POST) Exception {str(e)}")
            raise HTTPException(status_code=500, detail=str(e))


# Health Check endpoint
@app.get("/health")
async def health_check():
    logger.info("API endpoint for health status (GET) called.")
    return {"status": "UP"}
