#!/usr/bin/python

import populartimes
import json
import math
import requests
import geocoder



def my_current_location():
    g = geocoder.ip('me')
    my_location = g.latlng

    return my_location


# method 1
# def get_location_bound(lat, lon, distance):
#     R = 6378.1  # Radius of the Earth
#     brng = 1.57  # Bearing is 90 degrees converted to radians.
#     d = distance  # Distance in km
#
#     lat1 = math.radians(lat)  # Current lat point converted to radians
#     lon1 = math.radians(lon)  # Current long point converted to radians
#
#     lat2 = math.asin(math.sin(lat1) * math.cos(d / R) +
#                      math.cos(lat1) * math.sin(d / R) * math.cos(brng))
#
#     lon2 = lon1 + math.atan2(math.sin(brng) * math.sin(d / R) * math.cos(lat1),
#                              math.cos(d / R) - math.sin(lat1) * math.sin(lat2))
#
#     lat2 = math.degrees(lat2)
#     lon2 = math.degrees(lon2)
#
#     return lat2, lon2


# def get_radius_locations(mylocation, dist):
#     lat = mylocation["lat"]
#     lon = mylocation["lon"]
#
#     lat2, lon2 = get_location_bound(lat, lon, dist)
#     print(lat, lon, lat2, lon2)
#
#     data = populartimes.get(apiKey, ["bar"], (lat, lon), (lat2, lon2))
#     # print(data)
#     d = json.dumps(data, indent=2)
#     print(d)


# method 2
def get_nearby_id(location, rad, types):
    lat = location["lat"]
    lon = location["lon"]

    response = requests.get('https://maps.googleapis.com/maps/api/place/nearbysearch/json?'
                            'location=' + str(lat) + ',' + str(lon) + '&radius=' + str(rad) + '&type=' + types +
                            '&key=' + apiKey)
    res = response.json()
    for place in res["results"]:
        get_location_by_id(place["place_id"])


def get_location_by_id(place_id):
    place_details = populartimes.get_id(apiKey, place_id)
    print(json.dumps(place_details, indent=2))

"""
:param types: such bus_station,restaurant,hospital(https://developers.google.com/places/web-service/supported_types)
:param radius: define the the radius of the search
:param my_location: represent my current position
"""
if __name__ == "__main__":

    my_location = {"lat": my_current_location()[0], "lon": my_current_location()[1]}
    place_type = "bar"
    radius = 50000
    get_nearby_id(my_location, radius, place_type)

    # get_radius_location(loc, 50)

    # get_radius_location(mylocation, 50)
