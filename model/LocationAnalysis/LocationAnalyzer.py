from googleplaces import GooglePlaces, types, lang
import urllib

API_KEY = 'AIzaSyDs7GDvCjik1det8MPxe-RGbEmjq92BHYo'
RADIUS = 20
#LATITUDE = 53.345211
#LONGITUDE = -6.263378
ZERO = 0
TEST_COORDINATE_LIST = [(53.345211,-6.263378), (53.345211,-6.263378), (53.345999, -6.265052), (53.345999, -6.265052)]
# Define a dictionary with search term and return score
dic_place_types_scores = {'bar':1, 'restaurant':0.5}
PlaceTypeList = ['bar','restaurant'] # this list needs to be in order of most interest


class LocationAnalyzer():

    def __init__(self):
        print "Class Initialized"

    def VisitedPlaces(self, lat, lng):
        placesVisited = []

        google_places = GooglePlaces(API_KEY)
        location = {'lat': lat, 'lng': lng}

        query_result = google_places.nearby_search(
            lat_lng=location, radius=RADIUS)

        placesIds = []
        for place in query_result.places:
            # Returned places from a query are place summaries.
            placesIds.append(place.place_id)

        for placeid in placesIds:
            place_query_result = google_places.get_place(placeid)

            placeVisited = {
#                'formatted_address': place_query_result.formatted_address,
                'place_types': place_query_result.types
            }

            placesVisited.append(placeVisited)
            
        # Iterate through our list of placetypes of interest
        for search_place_type in PlaceTypeList:
            # Iterate through our list of places visited
            #print search_place_type
            for place_visited in placesVisited:
                # Iterate through the list of places types for the current place visited
                #print place_visited
                for returned_place_type in place_visited['place_types']:
                    # Check if the returned place type is one that we are searching for
                    #print returned_place_type
                    if returned_place_type == search_place_type:
                        #print 'match found'
                        # Get the return score from the dictionary
                        returned_score = dic_place_types_scores[search_place_type]
                        # Return the score
                        return returned_score


        return ZERO


lAnalyzer = LocationAnalyzer()
#results = lAnalyzer.VisitedPlaces(LATITUDE, LONGITUDE)
results = [] # list to hold the list of return values
# Iterate through our list of coordinates
for coordinate in TEST_COORDINATE_LIST:
    #result = lAnalyzer.VisitedPlaces(LATITUDE, LONGITUDE)
    lat = coordinate[0]
    lon = coordinate[1]
    result = lAnalyzer.VisitedPlaces(lat,lon)
    results.append(result)
#for result in results:
#    print result, '\t'
print results
