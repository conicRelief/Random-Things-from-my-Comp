__author__ = 'otto'

import os
import requests
import json
import calendar
import time
date = 0

weather_api_url = "http://api.openweathermap.org/data/2.5/history/"


def set_date(start_time_of_event):
    date = start_time_of_event
    pre_frame   =   4 #hours before event
    post_frame  =   2 #hours post event
    start = start_time_of_event - (pre_frame*60*60)
    end   = start_time_of_event + (post_frame*60*60)


def fetch_weather_data():
    #Supposed to return weather data
    pass


def format_URL_using_coordinate_information(lat , lon , start, end):
    return weather_api_url + 'city?lat=' + lat +"&lon="
def make_request_and_return_information():
    r = requests(format_URL_using_coordinate_information(weather_api_url))
    if r.status_code == 200:
        responseText = r.text
        print responseText
    else:
        print "Problem"