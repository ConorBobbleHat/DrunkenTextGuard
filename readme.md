DrunkenTextGuard

What is DrunkenTextGuard
How to setup
Gmail Context Gadget
Python
pip install contextio
pip install bottle
Azure Hosting
https://docs.microsoft.com/en-us/azure/app-service-web/app-service-web-get-started-python
Ensure you have Azure CLI (v2) installed
add voucher (or credit card) to your Amazon Account
How to create the model:

# Part 1 (Text Based):
    * Create a TextBasedClassifier object:
    t = TextBasedClassifier()
    * Train the data (only once - model expects drunk and not_drunk text files on the model data)
    df = t.TrainTextBasedClassifier()
    *Consume the model:
    t.Predict('I am drunk')


# Part 2 (Alyen Sentiment):
    #To DO

# Part 3 (Geolocator):
    #To DO
Contact GitHub 

-