import simplejson, urllib

import urllib, json
import pprint

import os 

import time
from time import sleep


GOOGLE_MAP_API_KEY=os.environ['GOOGLE_MAP_API_KEY']

def gets_rawjson_with_lat_lon(origin_lat, origin_lng, destination_lat, destination_lng):
	"""makes a call to gogole map to get the json data of two geolocations"""
	orig_coord = origin_lat, origin_lng
	dest_coord = destination_lat, destination_lng

	url = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&departure_time=now&traffic_model=best_guess&mode=transit&key={2}".format(str(orig_coord),str(dest_coord),str(GOOGLE_MAP_API_KEY))
	result= simplejson.load(urllib.urlopen(url))

	googleResponse = urllib.urlopen(url)
	jsonResponse = json.loads(googleResponse.read())
	return jsonResponse



def rawjson_into_miliseconds(rawjson):
	"""parses out json to get the duration time in miliseconds"""

	duration_time_raw =rawjson['routes'][0]['legs'][0]['duration']['text']
	duration_time_raw_split = duration_time_raw.split()

	if len(duration_time_raw_split) == 2:
		duration_time_hour = 0
		duration_time_min = duration_time_raw_split[0]
	if len(duration_time_raw_split) == 4:
		duration_time_hour = duration_time_raw_split[0]
		duration_time_min = duration_time_raw_split[2]

	hours = int(duration_time_hour)
	minutes = int(duration_time_min)
	miliseconds = int((3600000 * hours) + (60000 * minutes))

	return miliseconds

def transit_request_complete_milisecond_time(miliseconds):
	time_now = int(round(time.time() * 1000))
	future_time = time_now + int(miliseconds)
	return future_time



origin_lat = 37.785152
origin_lng = -122.406581
dest_lat = 37.762028
dest_lng = -122.47079

rawjson = gets_rawjson_with_lat_lon(origin_lat, origin_lng, dest_lat, dest_lng)
print "jsonResponse: ", rawjson
miliseconds = rawjson_into_miliseconds(rawjson)
print "miliseconds: ", miliseconds
future_time_miliseconds = transit_request_complete_milisecond_time(miliseconds)
print "future time miliseconds: ", future_time_miliseconds
