from fastapi import FastAPI
from transformers import pipeline

app=FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
	return {"message":"Hello, cat Mot!"}

@app.get("/predict/")
def predict():
	return classifier("I don't like you")[0]
