from bottle import route, run, template, default_app, request
import twilio.twiml

@route('/')
def text():
    body = request.query.Body
    words = body.split(" ")
    num = words.pop(0)
    body = " ".join(words)

    resp = twilio.twiml.Response()
    resp.message(num)
    return str(resp)

# This must be added in order to do correct path lookups for the views
import os
from bottle import TEMPLATE_PATH
TEMPLATE_PATH.append(os.path.join(os.environ['OPENSHIFT_REPO_DIR'], 'wsgi/views/')) 

application=default_app()