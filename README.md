# DrunkenTextGuard

Pitch from the "AI Hackathon: Ireland's First AI Hack - organized by Dublin AI" (https://www.meetup.com/DataScientistsIreland/events/237365278/)
Idea: prevent you from sending Drunk text messages.

## Example:
![Example](example.png)


## Model

Part 1 (Text Based):

	* Create a TextBasedClassifier object:
	t = TextBasedClassifier()
	* Train the data (only once - model expects drunk and not_drunk text files on the model data)
	df = t.TrainTextBasedClassifier()
	*Consume the model:
	t.Predict('I am drunk')

Part 2 (Geolocator):

	lAnalyzer = la.LocationAnalyzer()
	result = lAnalyzer.VisitedPlaces(lat,lon)


Part 3 (Alyen Sentiment):

	emotionGetter = aly.AylienEmotionClassifier()
    my_emotion_score = emotionGetter.getEmotion(text)    