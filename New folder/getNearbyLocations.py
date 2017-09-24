import urllib
import json
from pprint import pprint

API_KEY = "AIzaSyAT5yDn3sJ5Fqvm5MTijloIqYm1QeEIREA"

def getNearbyLocations(keyword, latitude, longitude):
	"""
	Given a latitude and longitude, queries the Google Places API to find the 5 locations nearest those coordinates
	matching the given keyword.
	"""

	query = ("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=" + str(latitude) + "," + str(longitude) 
		+ "&keyword=" + str(keyword) + "&rankby=distance" + "&key=" + str(API_KEY))

	response = urllib.urlopen(query)
	jsonRaw = response.read()
	jsonData = json.loads(jsonRaw)

	return [item for item in jsonData["results"] if jsonData["results"].index(item) < 5]


pprint(getNearbyLocations("hospital", 29.707836, -95.401563))

