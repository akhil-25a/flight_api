# Flight Search API

A **Flight Search API** built with **Django & Django REST Framework (DRF)**.  
This project allows searching flights with multiple filters using **dummy flight data**.

---

## 🛠 Features

- Search flights by **departure and arrival locations**  
- Filter by **price range**  
- Filter by **number of stops** (Non-stop, 1 stop, 2+ stops)  
- Filter by **departure/arrival time windows** (Morning, Afternoon, Evening, Night)  
- Filter by **WiFi availability**  
- Filter by **Inflight Meals**  
- Filter by **Aircraft Model** (e.g., Airbus A320, Boeing 737)  
- Filter by **Airlines** (with logos)  

All flight data is **manually input** for testing purposes.

api//
http://127.0.0.1:8000/api/flights/search/?from=Delhi&to=mumbai&stops=0&wifi=false

http://127.0.0.1:8000/api/flights/search/
