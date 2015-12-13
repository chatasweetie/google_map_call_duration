import simplejson, urllib

import urllib, json
import pprint

import os 



orig_lat = 37.7846810
orig_lng = -122.4073680
dest_lat = 37.761950
dest_lng = -122.470570


GOOGLE_MAP_API_KEY=os.environ['GOOGLE_MAP_API_KEY']

orig_coord = orig_lat, orig_lng
dest_coord = dest_lat, dest_lng

      
url = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&departure_time=now&traffic_model=best_guess&mode=transit&key={2}".format(str(orig_coord),str(dest_coord),str(GOOGLE_MAP_API_KEY))
result= simplejson.load(urllib.urlopen(url))

googleResponse = urllib.urlopen(url)
jsonResponse = json.loads(googleResponse.read())
pprint.pprint(jsonResponse)



dur =jsonResponse['routes'][0]['legs'][0]['duration']['text']

