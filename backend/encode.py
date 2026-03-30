import pickle
import pandas as pd

with open("models/encoder.pkl", "rb") as file:
    encoders = pickle.load(file)
    
def encode_input(data):
    encoded_data = pd.DataFrame([data])
    for column, encoder in encoders.items():
        if column in data:
            encoded_data[column] = encoder.transform([data[column]])[0]
        else:
            raise ValueError(f"Missing value for column: {column}")
    return encoded_data