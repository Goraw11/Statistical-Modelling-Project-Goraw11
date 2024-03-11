# Final-Project-Statistical-Modelling-with-Python

## Project/Goals

1. Fetching the data
   A. Send a request to CityBikes for the city of your choice.
   B. Parse through the response to get the details you want for the bike stations in that city (latitude, longitude, number of bikes).
   C. Put your parsed results into a DataFrame.

2. Connecting to Foursquare and Yelp APIs
3. Joining Data
4. Building a Model
 

## Process
Using the code below, I started off by Sending an API Request to City Bikes API, picked city of Hamilton, Ontario.
(I had to ensure that I do not get 

```
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
    
    # Create lists to store parsed data
    station_names = []
    latitudes = []
    longitudes = []
    bikes_available = []
    
    # Parse data and store in lists
    for station in stations:
        station_names.append(station['name'])
        latitudes.append(station['latitude'])
        longitudes.append(station['longitude'])
        bikes_available.append(station['free_bikes'])
    
    # Create DataFrame from parsed data
    df = pd.DataFrame({
        'Station Name': station_names,
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Bikes Available': bikes_available
    })
    
    # Print DataFrame
    print(df)
else:
    # Handle errors
    print(f'Error: {response.status_code} - {response.text}')
```



## Results
(fill in what you found about the comparative quality of API coverage in your chosen area and the results of your model.)

## Challenges 
(discuss challenges you faced in the project)

## Future Goals
(what would you do if you had more time?)
