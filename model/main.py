#WD: 'C:\\git\\DrunkenTextGuard\\model'
import TextBasedClassifier.TextBasedClassifier as tb

class MainModel():
    
    def __init__(self):
        pass
    
    def predict(self, text):
        
        M1_weight = 1
        M2_weight = 0
        M3_weight = 0
        
        #Model1: Text Based Classifier
        m1 = tb.TextBasedClassifier()
        #m1.TrainTextBasedClassifier() only once
        p1 = round ( float(m1.Predict(text)["Prob_1"]) ,2 )
        
        
        p2 = 0
        
        p3 = 0
        
        p = p1 * M1_weight + p2 * M2_weight + p3 * M3_weight

        return 'There is a {0:.0f}% chance you are drunk!'.format(p*100)
    