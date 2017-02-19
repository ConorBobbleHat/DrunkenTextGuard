#WD: 'C:\\git\\DrunkenTextGuard\\model'
import TextBasedClassifier.TextBasedClassifier as tb

class MainModel():
    
    def __init__(self):
        pass
    
    def predict(self, text):
        
        #Model1: Text Based Classifier
        m1 = tb.TextBasedClassifier()
        #m1.TrainTextBasedClassifier() only once
        p1 = round ( float(m1.Predict(text)["Prob_1"]) ,2 )

        return 'There is a {0:.0f}% chance you are drunk'.format(p1*100)