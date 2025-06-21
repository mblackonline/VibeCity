# Local Music Awareness App

**Increase awareness and discovery of local music using open source software!**

## Overview

This project is an open source application dedicated to promoting and increasing awareness of local music scenes. By leveraging community-driven data and open technology, music lovers can discover new artists, venues, and events in their area, helping to support independent musicians and foster vibrant local music communities.

## 📝 Data Source

Event data used in this project was sourced from the [Chattanooga Music Guide](https://chattanoogamusicguide.com/), a valuable resource for discovering live music in the Chattanooga area.

We thank them for curating and sharing this information to help promote the local music scene.

## Features

- **Local Artist Discovery:** Find local musicians and bands.
- **Event Listings:** Explore upcoming music events near you.
- **Venue Directory:** Browse local venues.
- **Open Data:** All music and event data is contributed by the community and available under open licenses.
- FUTURE: **Community Contributions:** Musicians, venues, and fans can submit updates and new info.

## Acknowledgments

- Thanks to all local artists, venues, and music lovers who make this possible!
- Inspired by open culture and community-driven projects.

---
<br>

# Events API Documentation

## Overview
This API provides endpoints for managing and querying musical events data. It supports retrieving all events, upcoming events, searching by artist, and filtering by date.

## Data Model
```python
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    """Represents a musical event."""
    venue: str        # Name of the performance venue
    artist: str       # Performing artist/group
    date: datetime    # Date and time of the event
    url: str          # Ticket purchase or event details URL
```

## API Endpoints

### 1. Get All Events
* **Endpoint:** `/events`
* **Method:** GET
* **Response:** List of all events
* **Example Response:**
```json
[
    {
        "venue": "Barking Legs",
        "artist": "Dexter Bell & Friends",
        "date": "2025-06-18T00:00:00",
        "url": "https://www.barkinglegs.org/..."
    }
]
```

### 2. Get Upcoming Events
* **Endpoint:** `/events/upcoming`
* **Method:** GET
* **Response:** List of events occurring within the next 60 days
* **Parameters:** None
* **Example Response:** Same format as `/events`

### 3. Search Events by Artist
* **Endpoint:** `/events/search`
* **Method:** GET
* **Parameters:**
  * `artist`: string (required)
    * Description: Artist name to search for
    * Example: `/events/search?artist=Cowboy%20Mouth`
* **Response:** List of events matching the artist name (case-insensitive)

### 4. Get Events by Date
* **Endpoint:** `/events/by-date`
* **Method:** GET
* **Parameters:**
  * `date`: datetime (required)
    * Format: YYYY-MM-DD
    * Example: `/events/by-date?date=2025-07-11`
* **Response:** List of events occurring on the specified date

## Usage Examples
```bash
# Get all events
curl http://your-api-url/events

# Get upcoming events
curl http://your-api-url/events/upcoming

# Search for events by artist
curl 'http://your-api-url/events/search?artist=Cowboy%20Mouth'

# Get events for a specific date
curl 'http://your-api-url/events/by-date?date=2025-07-11'
```

*Let’s build a stronger local music scene together!*
