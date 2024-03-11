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

I then packaged the results nicely into a CSV file.
```
df.to_csv('..\\data\\available_bikes.csv', index=False)
```

Following that, I moved over to fetch data from Foursquare and Yelp, by using my API Keys for authorization. I also created a test function first, just to ensure that a '200' (success) reply is returned.
(Here, I had to insert the 'for' function, so as to ensure that my API doesn't get blocked for repeatedly trying to fetch the data).

Foursquare:
```
#get data from the FS API
def get_venues_fs(latitude, longitude, radius, api_key, categories):
    """
    Get venues from foursquare with a specified place type and coordinates.
    Args:
        latitude (float): latitude for query (must be combined with longitude)
        longitude (float): longitude for query (must be combined with latitude)
        api_key (str): foursquare API to use for query
        categories (str) : Foursquare-recognized place type. If not passed no place_type will be specified. Separate ids with commas
    
    Returns:
        response: response object from the requests library.
    """
    # create the URL
    url = "https://api.foursquare.com/v3/places/search"
    # create the parameters
    params = {
        "ll" : f"{latitude},{longitude}",
        "radius" : radius,
        "categories" : categories,

    }
    # create the headers
    headers = {
        "accept": "application/json",
        "Authorization": api_key
        }
    # make the request
    resp = requests.get(url=url, params=params, headers=headers)
    # return the response
    return resp
```

Yelp:
```import requests

# Define the function to get venues from Yelp
def get_venues_yelp(latitude, longitude, radius, api_key, categories=None):
    """
Get venues from foursquare with a specified place type and coordinates.
    Args:
        latitude (float): Latitude for the query (must be combined with longitude).
        longitude (float): Longitude for the query (must be combined with latitude).
        radius (int): Search radius in meters.
        api_key (str): Yelp API key to use for the query.
        categories (str): Yelp-recognized place types. If not passed, no place_type will be specified. Separate ids with commas.
    
    Returns:
        response: Response object from the requests library.
    """
    # Create the URL
    url = "https://api.yelp.com/v3/businesses/search"
    
    # Create the parameters
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "radius": radius
    }
    
    # If categories are provided, add them to the parameters
    if categories:
        params["categories"] = categories
    
    # Create the headers with the correct authorization format
    headers = {
        "Authorization": f"Bearer {api_key}"
    }
    
    try:
        # Send the GET request to Yelp API
        response = requests.get(url, params=params, headers=headers)
        
        # Check the response status code
        print(response.status_code)
        
        # Return the response
        return response
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to get venues from Yelp
response = get_venues_yelp(latitude, longitude, radius, api_key, categories)

# Check the response status code
print(response.status_code)

# Print the response text
print(response.text)
```

For both Yelp and Foursquare API Queries:
- I brought in available_bikes over
- Parsed thru the responses to get POIs
- Created a Function to query for venues near a given location and tested it
- Created a dataframe with the parsed results
- Packaged the results into a nice CSV
- compared the results
- Listed top 10 restaurants according to their name and rating
```
# Sort the DataFrame by the ratings column in descending order, then by name alphabetically
top_restaurants = flattenedYELPdata.sort_values(by=['rating', 'name'], ascending=[False, True])

# Select the top 10 restaurants
top_10_restaurants = top_restaurants.head(10)

# Display the top 10 restaurants
print("Top 10 restaurants:")
print(top_10_restaurants[['name', 'rating']])
```

## Results
I found out that the API Coverage for YELP is much more robust and informative as compared to Foursquare. Both show good information, however, YELP has:
- more information
- more details
- is at a more granular level

## Challenges 
The biggest challenge was, and where I spent most time, was on the API query section. I had a lot of difficulty sending out queries to get the right behaviour (and data packages) from all 3 of the APIs.

## Future Goals
- I would spend a lot more time on the EDA - exploratory Data Analysis process
- I would create some questions myself which I would like to get answers for
- I would generate more insights
- I will also use more visual tools to convey the data and the insights
