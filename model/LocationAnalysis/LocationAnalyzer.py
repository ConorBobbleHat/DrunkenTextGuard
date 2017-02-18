from googleapiclient.discovery import build
from googleplaces import GooglePlaces, types, lang
import urllib

API_KEY = 'AIzaSyDs7GDvCjik1det8MPxe-RGbEmjq92BHYo'

class LocationAnalyzer():
    def __init__(self):
        print "Class Initialized"

    def HasBeenInABar(self, lat, long):
        google_places = GooglePlaces(API_KEY)
        
        query_result = google_places.nearby_search(
            location='London, England', keyword='Fish and Chips',
            radius=20000, types=[types.TYPE_FOOD])

lAnalyzer = LocationAnalyzer()
lAnalyzer.HasBeenInABar(1, 2)


