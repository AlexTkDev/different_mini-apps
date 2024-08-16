import httpx
from fastapi import FastAPI

app = FastAPI(debug=True)


@app.get("/")
async def root():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://official-joke-api.appspot.com/random_joke")
        if response.status_code == 200:
            joke = response.json()
            return joke
        else:
            return {"error": "Failed to fetch the joke"}

# uvicorn your_script_name:app --reload
