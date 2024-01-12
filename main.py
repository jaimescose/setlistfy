from fastapi import FastAPI
import requests

from config import get_settings


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/setlists/{setlist_id}")
def read_setlist(setlist_id: str):
    settings = get_settings()
    response = requests.get(f'https://api.setlist.fm/rest/1.0/setlist/{setlist_id}', headers={'x-api-key': settings.SETLIST_FM_API_KEY, 'Accept': 'application/json'})
    return response.json()
