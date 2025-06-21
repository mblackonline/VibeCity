from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List
from datetime import datetime, timedelta
import json

app = FastAPI()

# Define the data model
class Event(BaseModel):
    venue: str
    artist: str
    date: datetime
    url: str

# Load events from JSON file
with open("event_data.json") as f:
    raw_data = json.load(f)
    events = [Event(**item) for item in raw_data]

@app.get("/events", response_model=List[Event])
def get_all_events():
    return events

@app.get("/events/upcoming", response_model=List[Event])
def get_upcoming_events():
    today = datetime.today()
    two_months = today + timedelta(days=60)
    return [event for event in events if today <= event.date <= two_months]

@app.get("/events/search", response_model=List[Event])
def search_by_artist(artist: str = Query(..., description="Artist name to search for")):
    return [event for event in events if artist.lower() in event.artist.lower()]

@app.get("/events/by-date", response_model=List[Event])
def search_by_date(
    date: datetime = Query(..., description="Date in YYYY-MM-DD format")
):
    return [event for event in events if event.date.date() == date.date()]
