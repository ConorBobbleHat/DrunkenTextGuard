from bottle import route, run, template, default_app, request
import twilio.twiml
import os
import model

t = model.TextBasedClassifier.TextBasedClassifier.TextBasedClassifier()
df = t.TrainTextBasedClassifier()

@route('/')
def text():
    body = request.query["Body"]
    words = body.split(" ")

    num = words.pop(0)
    body = " ".join(words)
    resp = twilio.twiml.Response()
    resp.message(num)
    return str(resp)

run(host='0.0.0.0',port=8080)