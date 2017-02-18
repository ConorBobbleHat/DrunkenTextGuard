from TextBasedClassifier import TextBasedClassifier


class Model():
    t2=TextBasedClassifier()
    df = t2.TrainTextBasedClassifier()
    s = t2.Predict('I am drunk')
    
    s['Prob_0']
    s['Prob_1']
    #    