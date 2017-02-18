from bottle import route, run, template, default_app, request
import twilio.twiml

@route('/')
def text():
    #body = request.query["Body"]
    #words = body.split(" ")

    #num = words.pop(0)
    #body = " ".join(words)
    resp = twilio.twiml.Response()
    resp.message("Hello")
    return str(resp)

run(host='127.0.0.1',port=8080)