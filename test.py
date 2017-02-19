import model.TextBasedClassifier.TextBasedClassifier as tb
import model.main as m
import model.LocationAnalysis.LocationAnalyzer as la
import model.AylienApi.AylienEmotionClassifier as aly

#Only once
t = tb.TextBasedClassifier()
df = t.TrainTextBasedClassifier()

body = 'hellou honney, I will stop by in five minutes'
    
predictor = m.MainModel()
prediction = predictor.predict(body) 

print prediction




TEST_COORDINATE_LIST = [(53.345211,-6.263378), (53.345211,-6.263378), (53.345999, -6.265052), (53.345999, -6.265052)]


lAnalyzer = la.LocationAnalyzer()
la.TEST_COORDINATE_LIST = TEST_COORDINATE_LIST

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




