import TextBasedClassifier.TextBasedClassifier as tb
import model.LocationAnalysis.LocationAnalyzer as la
import model.AylienApi.AylienEmotionClassifier as aly
import numpy as np

class MainModel():
    
    def __init__(self):
        pass
    
    text = 'I HATE YOU'
    def predict(self, text):
        
        M1_weight = 0.5
        M2_weight = 0.5
        
        #Model1: Text Based Classifier
        m1 = tb.TextBasedClassifier()
        #m1.TrainTextBasedClassifier() only once
        p1 = round ( float(m1.Predict(text)["Prob_1"]) ,2 )
                
        
        
        
        TEST_COORDINATE_LIST = [(53.345211,-6.263378), (53.345211,-6.263378), (53.345999, -6.265052), (53.345999, -6.265052)]       
        lAnalyzer = la.LocationAnalyzer()
        la.TEST_COORDINATE_LIST = TEST_COORDINATE_LIST        
        results = [] # list to hold the list of return values
        for coordinate in TEST_COORDINATE_LIST:            
            lat = coordinate[0]
            lon = coordinate[1]
            result = lAnalyzer.VisitedPlaces(lat,lon)
            results.append(result)
        p2 = np.average(results)
        
        
        emotionGetter = aly.AylienEmotionClassifier()
        my_emotion_score = emotionGetter.getEmotion(text)        
        p3 = 0
        extra_msg = ''
        if str(my_emotion_score[0]) in ['anger', 'hate', 'worry']:
            p3 = 0.1
            extra_msg = ' I also believe you are expressing {}'.format(str(my_emotion_score[0]))
        

        p = p1 * M1_weight + p2 * M2_weight + p3

        return 'There is a {0:.0f}% chance you are drunk!'.format(p*100) + extra_msg
    