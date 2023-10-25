import json
import requests

print("hello world")
# Define a business ID
business_id = 'qQGoakW5_M2Dtu1rBz7u-g'

ans = input("search or match a resturant?: ").lower()
while True:
    if ans =="search" or "match":
        if ans == "search":
            ENDPOINT = 'https://api.yelp.com/v3/businesses/search'
        elif ans == "match":
            ENDPOINT = 'https://api.yelp.com/v3/businesses/matches'
        break
    else:
        print("invaild answer, try again.")
# Define my API Key, My Endpoint, and My Header
API_KEY = 'xHEZ0ttl4fZpm5smHhp7GqAVJ_Dz6CLjgPbgKQCm2KSs_eYs_DXiNCp6X0pesy6PI5bg0gmOipZffhCxAo6STEOa7RbvSDvzUyoHcw5qB0MMgnXXXbAPFCEZGvkMZXYx'
ENDPOINT = ENDPOINT.format(business_id)
HEADERS = {'Authorization': 'bearer %s' % API_KEY}

# Define my parameters of the search
# BUSINESS SEARCH PARAMETERS - EXAMPLE
TERM = input("enter a term:")
LIMIT = 10 #input("enter a limit of results:")
CATEGORIES = input("enter a catergory:")
LOCATION = input("enter a location:")
RATING = float(input("enter rating number: "))
RADIUS = 10000 #input("enter a number of radius:")
PARAMETERS = {'term': TERM,
              'limit': LIMIT,
              'radius': RADIUS,
              'catergories': CATEGORIES,
              'location': LOCATION}

# BUSINESS MATCH PARAMETERS - EXAMPLE
#PARAMETERS = {'name': 'Peets Coffee & Tea',
#              'address1': '7845 Highland Village Pl',
#              'city': 'San Diego',
#              'state': 'CA',
#              'country': 'US'}

# Make a request to the Yelp API
response = requests.get(url = ENDPOINT,
                        params = PARAMETERS,
                        headers = HEADERS)

# Conver the JSON String to a dict object
business_data = response.json()

# print the response
#print(json.dumps(business_data, indent = 3)) 

#print business names
x=0
for biz in business_data['businesses']:
    if float(biz['rating'])>= RATING:
        x+=1
        print(biz['name'])
        print("rating: ", biz['rating'])
if x==0: 
    print("sorry no resturants match the criterias")
