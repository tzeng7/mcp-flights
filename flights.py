from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("flights")

@mcp.tool()
def find_flights(start: str, 
                 end: str,
                 departure_date: str,
                 return_date: str = None,
                 passengers: int = 1,
                 economy_class: str = "economy",
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
    
    serp_api = "https://serpapi.com/search?engine=google_flights"
    
    
    
    
