import simplejson, urllib

import json
import pprint

import os

import time
from time import sleep

import datetime


GOOGLE_MAP_API_KEY=os.environ['GOOGLE_MAP_API_KEY']


def gets_rawjson_with_lat_lon(origin_lat, origin_lng, destination_lat, destination_lng):
    """makes a call to gogole map to get the json data of two geolocations"""
    orig_coord = origin_lat, origin_lng
    dest_coord = destination_lat, destination_lng

    url = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&departure_time=now&traffic_model=best_guess&mode=transit&key={2}".format(str(orig_coord),str(dest_coord),str(GOOGLE_MAP_API_KEY))
    result = simplejson.load(urllib.urlopen(url))

    googleResponse = urllib.urlopen(url)
    jsonResponse = json.loads(googleResponse.read())
    return jsonResponse


def rawjson_into_datetime(rawjson):
    """parses out json to get the datetime of arrival time"""

    arrival_time_raw = rawjson['routes'][0]['legs'][0]['arrival_time']['text']
    arrival_time_raw_split = arrival_time_raw.split(":")

    if arrival_time_raw[-2:] == "pm":
        arrival_time_hour = 12

    arrival_time_hour += int(arrival_time_raw_split[0])
    arrival_time_min = arrival_time_raw_split[1][:-2]

    hours = int(arrival_time_hour)
    minutes = int(arrival_time_min)

    now = datetime.datetime.now()

    arrival_time = now.replace(hour=hours, minute=minutes)

    return arrival_time





origin_lat = 37.785152
origin_lng = -122.406581
dest_lat = 37.762028
dest_lng = -122.47079

rawjson = gets_rawjson_with_lat_lon(origin_lat, origin_lng, dest_lat, dest_lng)
print "jsonResponse: ", rawjson
arrival_time = rawjson_into_datetime(rawjson)
print "arrival_time: ", arrival_time
