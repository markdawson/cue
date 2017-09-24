from pprint import pprint

API_KEY = "AIzaSyCBENbTvT2yE0_53Czgu-nuhb7ahq-fgig"

def getDirections(current_latitude, current_longitude, destination__latitude, destination__longitude):
	"""
	Given latitude and longitude of a user's current location as well as the latitude and longitude of their destination, returns
	a URL to the Google Maps page for directions from their current location to their destination.
	"""

	query = 'https://www.google.com/maps/dir/' + str(current_latitude) + ',' + str(current_longitude) +'/' + str(destination__latitude) + ',' + str(destination__longitude)

	print query


