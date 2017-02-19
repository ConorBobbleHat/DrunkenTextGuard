import model.TextBasedClassifier.TextBasedClassifier as tb
import model.main as m



#Only once
t = tb.TextBasedClassifier()
df = t.TrainTextBasedClassifier()

body = 'I dont think Im sober'
    
predictor = m.MainModel()
prediction = predictor.predict(body) 

print prediction