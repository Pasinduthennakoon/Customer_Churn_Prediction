from fastapi import FastAPI
from schema.schema_model import ChurnPredictionRequest
from encode import encode_input
import pickle

with open("models/customer_churn_model.pkl", "rb") as file:
    model_data = pickle.load(file)

loaded_model = model_data['model']
feature_names = model_data['feature_names']

app = FastAPI()

@app.post('/predict')
def predict_churn(request: ChurnPredictionRequest):
    
    data = encode_input(request.dict())
    
    predct = loaded_model.predict(data)
    pred_prob = loaded_model.predict_proba(data)
    
    return {
    "churn_prediction": int(predct[0]),
    "churn_probability": float(pred_prob[0][1])
}