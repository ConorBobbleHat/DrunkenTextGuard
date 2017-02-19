import urllib, urllib2
import json

from aylienapiclient import textapi


class AylienEmotionClassifier():
    def __init__(self):
        print "## Aylien initialized"

    def getEmotion(self, sentence):
        """ Inputs a sentence and returns a tuple (<emotion>, <score>)
        """

        url = 'http://production.tap.aylien.com/e93bd452-e39a-4630-8db0-9138a8a10c91'
        headers = {'x-aylien-tap-application-key': '375bc23e29cf4a0c861a29a8c86e393f'}

        data = urllib.urlencode({"text": sentence})
        req = urllib2.Request(url, data, headers)
        response = urllib2.urlopen(req)
        result = response.read()

        data = json.loads(result)
        emotionScore = (data["categories"][0]['id'], data["categories"][0]['confidence'])

        return emotionScore


if(__name__ == "main"):
    emotionGetter = AylienEmotionClassifier()
    my_emotion_score = emotionGetter.getEmotion("I hate you")
    print my_emotion_score
