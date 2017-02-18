from TextBasedClassifier import TextBasedClassifier


class Model():
    
    t2=TextBasedClassifier()
    #call df = t2.TrainTextBasedClassifier() only once
    s = t2.Predict('I am drunk')
    print s
    
