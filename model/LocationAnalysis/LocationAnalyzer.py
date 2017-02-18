from googleapiclient.discovery import build
from googleplaces import GooglePlaces, types, lang
import urllib

API_KEY = 'AIzaSyDs7GDvCjik1det8MPxe-RGbEmjq92BHYo'

class LocationAnalyzer():
    def __init__(self):
        print "Class Initialized"

    def VisitedPlaces(self, lat, lng):
        placesVisited=[];

        google_places = GooglePlaces(API_KEY)
        location = { 'lat': lat, 'lng': lng}

        query_result = google_places.nearby_search(lat_lng=location, radius=100)
        
        placesIds = [];
        for place in query_result.places:
            # Returned places from a query are place summaries.
            placesIds.append(place.place_id)

        for placeid in placesIds:
            place_query_result = google_places.get_place(placeid)
            
            placeVisited = {
                'formatted_address': place_query_result.formatted_address,
                'place_types': place_query_result.types
                };

            placesVisited.append(placeVisited);

        return placesVisited;


lAnalyzer = LocationAnalyzer()
results = lAnalyzer.VisitedPlaces(53.3452026, -6.2642727)
for result in results:
    print result,'\t'
