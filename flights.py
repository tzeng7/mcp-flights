from mcp.server.fastmcp import FastMCP
import requests
from serpapi import GoogleSearch
from dotenv import load_dotenv
import os

load_dotenv()
serp = os.getenv("SERPAPI")
mcp = FastMCP("flights")

@mcp.tool()
def find_flights(start: str, 
                 end: str,
                 departure_date: str,
                 return_date: str = None,
                 passengers: int = 1,
                 travel_class: str = "economy",
                 max_price: float = None,
                 max_stops: int = None,
                 airline: str = None):
    """
    Search for flights between the starting location and the destination.
    
    Args:
        start: Origin airport code ('LAX', 'JFK')
        end: Destination airport code
        departure date: Departure Date (YYYY-MM-DD)
        return date: Return Date (optional YYYY-MM-DD)
        passengers: Number of passengers (default: 1)
        economy class: Travel class (default: economy)
        max price: Maximum price of the plane flight ticket
        max stops: Maximum number of stops the flight takes
        airline: Airline name
    """
    
    params = {
        "engine": "google_flights",
        "departure_id": start,
        "arrival_id": end,
        "outbound_date": departure_date,
        "return_date": return_date,
        "currency": "USD",
        "travel_class": travel_class,
        "stops": max_stops,
        "max_price": max_price,
        "hl": "en",
        "api_key": serp
    }    
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        return results
    except Exception as e:
        print(f"Flight search failed. {e}")
        

        
        
    
    
    
    
    
    
