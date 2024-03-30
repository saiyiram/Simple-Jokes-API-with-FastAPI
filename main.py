from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
import random
import json

app = FastAPI()

with open('jokes.json', 'r') as file:
    jokes = json.load(file)

class Joke(BaseModel):
    id: int
    jokeText: str
    jokeType: str

@app.get("/random")
async def get_random_joke():
    random_index = random.randint(0, len(jokes) - 1)
    return jokes[random_index]

@app.get("/jokes/{id}")
async def get_joke(id: int):
    for joke in jokes:
        if joke["id"] == id:
            return joke
    raise HTTPException(status_code=404, detail="Joke not found")

@app.get("/filter")
async def filter_jokes(type: Optional[str] = None):
    if type:
        return [joke for joke in jokes if joke["jokeType"] == type]
    return jokes

@app.post("/jokes")
async def create_joke(joke: Joke):
    joke.id = len(jokes) + 1
    jokes.append(joke.dict())
    return joke

@app.put("/jokes/{id}")
async def update_joke(id: int, joke: Joke):
    for index, existing_joke in enumerate(jokes):
        if existing_joke["id"] == id:
            jokes[index] = joke.dict()
            return jokes[index]
    raise HTTPException(status_code=404, detail="Joke not found")

@app.patch("/jokes/{id}")
async def partial_update_joke(id: int, joke: Joke):
    for index, existing_joke in enumerate(jokes):
        if existing_joke["id"] == id:
            updated_joke = existing_joke.copy()
            updated_joke.update(joke.dict(exclude_unset=True))
            jokes[index] = updated_joke
            return jokes[index]
    raise HTTPException(status_code=404, detail="Joke not found")

@app.delete("/jokes/{id}")
async def delete_joke(id: int):
    for index, joke in enumerate(jokes):
        if joke["id"] == id:
            del jokes[index]
            return {"detail": "Joke deleted"}
    raise HTTPException(status_code=404, detail="Joke not found")

@app.delete("/all")
async def delete_all_jokes(key: Optional[str] = None):
    if key == "masterKey": # Replace "masterKey" with your actual master key
        jokes.clear()
        return {"detail": "All jokes deleted"}
    raise HTTPException(status_code=403, detail="You are not authorized to perform this action.")
