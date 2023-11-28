# geocoding_helper.py

import requests

def get_location_coordinates(location):
    """
    Get the latitude and longitude coordinates for a given location using the OpenCage Geocoding API.

    Args:
        location (str): The location for which you want coordinates.

    Returns:
        dict: A dictionary containing 'latitude' and 'longitude'.
    """
    api_key = "fa0a9951d81d47869157ca431fab2b9b"
    base_url = "https://api.opencagedata.com/geocode/v1/json"
    
    params = {
        'key': api_key,
        'q': location,
        'limit': 1  # You can adjust the limit based on your requirements
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    if response.status_code == 200 and data.get('results'):
        # Extracting coordinates from the response
        lat = data['results'][0]['geometry']['lat']
        lon = data['results'][0]['geometry']['lng']
        return {'latitude': lat, 'longitude': lon}
    else:
        # Handle errors appropriately
        print(f"Error: {data['status']['message']}")
        return None
