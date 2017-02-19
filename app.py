from bottle import route, run, template, default_app, request
import twilio.twiml
import os
import model.TextBasedClassifier.TextBasedClassifier as tb
import model.main as m



#Only once
t = tb.TextBasedClassifier()
df = t.TrainTextBasedClassifier()

#a = model.AylienApi.AylienEmotionClassifier.AylienEmotionClassifier()

@route('/')
def text():
    body = request.query["Body"]
    #words = body.split(" ")

    #num = words.pop(0)
    #body = " ".join(words)   
    resp = twilio.twiml.Response()
    
    predictor = m.MainModel()
    prediction = predictor.predict(body) 
    #emotion = a.getEmotion(body)
    resp.message(str(prediction)) #+ str(emotion))
    return str(resp)

run(host='0.0.0.0',port=8080)