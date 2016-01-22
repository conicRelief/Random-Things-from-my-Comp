import requests
import json
import calendar
import time
import os.path
import sys
import datetime
import time 


def getContent(source):
	file = open(source, 'r')
	content = file.read()
	file.close()
	return content

def storeContent(source, content):
	file = open(source, 'w')
	file.write(content)
	file.close()

def formatUrlWithLatLon(url,lat,lon):
	return url + "weather?lat=" + str(lat) + "&lon=" +str(lon)
	


nameOfTrackFile = "race_tracks.json"
openWeatherApi = "http://api.openweathermap.org/data/2.5/"




content = getContent(nameOfTrackFile)

encoded_json = json.loads(content)

for x,obj in enumerate(encoded_json["tracks"]):
	coordinates = obj["coordinates"][0]
	lat = coordinates[1]
	lon = coordinates[0]
	print "Coordinates::: Lat: ", lat , ", Lon: ", lon  
	url = formatUrlWithLatLon(openWeatherApi,lat,lon)
	print x,url
	print "MakingRequest"
	response = requests.get(url)
	encoded_response = json.loads(response.text)
	try:
		encoded_json["tracks"][x]["weather"] =encoded_response["weather"]
	except:
		print "				No Weather"
	try:
		encoded_json["tracks"][x]["main"] = encoded_response["main"]
	except:
		print "				No Main"


textDump = json.dumps(encoded_json, indent = 4)

storeContent(nameOfTrackFile, textDump)

