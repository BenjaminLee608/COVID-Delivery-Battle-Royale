import pprint
import time
import googlemaps
import pgeocode
import json

"""
# pause script for 3 seconds
time.sleep(3)

# get next 20 results

places_result = gmaps.places_nearby(page_token = places_result['next_page_token'])

pprint.pprint(places_result)
"""

# loop through each place in the results

print('Welcome to COVID-19 Delivery Battle Royale! This program allows you to search all the nearby delivery places that are open right now (within 4 miles)!')
print('You will be given 2 choices for delivery and you will pick the place you\'d rather eat at. The place you like more will go on to the next round, and the other will be eliminated.')
print('A new delivery place will challenge the winner, and this will repeat until there is only one delivery place!')

print('\nWhenever you are ready, please type k to start, or q to quit')

input_start = input()
if input_start == 'q':
	exit()
while(input_start != 'k'):
	input_start = input('Type k when you are ready to start, or q to quit')
	if input_start == 'q':
		exit()

input_zip = input('Please enter your zip/postal code: ')

#GETS googlemaps Client, and places_result
nomi = pgeocode.Nominatim('us')
location = nomi.query_postal_code(input_zip)
latlon = str(location.latitude) + "," + str(location.longitude)

# Define API Key    
API_KEY = "AIzaSyCMa0dg1A1NF-4qs_dVt7FgNoHNgC9PxY8"

# Define our client
gmaps = googlemaps.Client(key = API_KEY)

# Define Search
places_result = gmaps.places_nearby(latlon, radius = 6437, open_now = True, type = 'meal_delivery')


	

first = True

for place in places_result['results']:

    # define my place id
    my_place_id = place['place_id']

    # define the fields we want sent back to us
    my_fields = ['name', 'formatted_phone_number', 'formatted_address']

    # make request for the details
    place_details = gmaps.place(place_id = my_place_id, fields = my_fields)

    #print results
    if first:
    	first_choice = place_details
    	first = False
    	continue
    second_choice = place_details

    #pprint.pprint(first_choice)
    print()
    print('Choice 1:')
    print("Name:",first_choice['result']['name'])
    print("Address:",first_choice['result']['formatted_address'])
    print("Phone Number:",first_choice['result']['formatted_phone_number'])
    print()
    #pprint.pprint(second_choice)
    print('Choice 2:')
    print("Name:",second_choice['result']['name'])
    print("Address:",second_choice['result']['formatted_address'])
    print("Phone Number:",second_choice['result']['formatted_phone_number'])

    user_input = input('Which would you rather prefer? (1 or 2) ')

    while (user_input != '1' and user_input != '2'):
    	user_input = input('Which would you rather prefer? (1 or 2) ')

    if(user_input == '2'):
    	first_choice = second_choice
    print()

print('You\'ve chosen:',first_choice['result']['name'])
print("Address:",first_choice['result']['formatted_address'])
print("Phone Number:",first_choice['result']['formatted_phone_number'])