from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def root():
	return{'message':"Маргарита Бабий - бездельница и лежебока, хочет стать котом"}
