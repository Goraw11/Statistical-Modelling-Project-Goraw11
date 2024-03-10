import requests

# Define the API endpoint URL to retrieve data for the SOBI Hamilton network
url = "http://api.citybik.es/v2/networks/sobi-hamilton"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Extract hrefs for each city (not applicable in this context)
    # Print the entire data for the SOBI Hamilton network
    print(data)
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')




import requests

# Define the API endpoint URL to retrieve data for the SOBI Hamilton network
url = "http://api.citybik.es/v2/networks/sobi-hamilton"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract station details
    stations = data['network']['stations']
    
    # Print details for each station
    for station in stations:
        # Extract station name, latitude, longitude, and number of bikes
        name = station['name']
        latitude = station['latitude']
        longitude = station['longitude']
        bikes_available = station['free_bikes']
        
        # Print station details
        print(f"Station: {name}, Latitude: {latitude}, Longitude: {longitude}, Bikes available: {bikes_available}")
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')



import requests
import pandas as pd

# Define the API endpoint URL to retrieve data for the SOBI Hamilton network
url = "http://api.citybik.es/v2/networks/sobi-hamilton"

# Make the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Extract station details
    stations = data['network']['stations']
    
    # Find station details for "City Hall" station
    city_hall_station = None
    for station in stations:
        if station['name'] == "City Hall":
            city_hall_station = station
            break
    
    # Check if "City Hall" station was found
    if city_hall_station:
        # Extract station details
        name = city_hall_station['name']
        latitude = city_hall_station['latitude']
        longitude = city_hall_station['longitude']
        bikes_available = city_hall_station['free_bikes']
        
        # Create DataFrame with station details
        df = pd.DataFrame({
            'Station Name': [name],
            'Latitude': [latitude],
            'Longitude': [longitude],
            'Bikes Available': [bikes_available]
        })
        
        # Print DataFrame
        print(df)
    else:
        print("City Hall station not found.")
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')
