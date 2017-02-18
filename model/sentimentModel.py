import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import operator


################################### READ TRAINING DATA
df = pd.DataFrame([
                    ['Hello how are you?',0], 
                    ['feck off you idiot',1],
                    ['I AM NOT DRUNK',1]
                    ], columns=['message', 'status'])



################################### PREPARE TRAINING DATA

#2)Create and fit the CountVectorizer
cv = CountVectorizer(stop_words='english', max_features=400) #vocabulary=['hot', 'cold', 'old'] 

#3)Get the geature Matrix
featuresMatrix = cv.fit_transform(df["message"]).toarray()
#featuresMatrix = cv.fit_transform(dfall[dfall['interest_level'] == 'medium']["features2"]).toarray()
 
 
word_freq_df = pd.DataFrame({'term': cv.get_feature_names(), 'occurrences':np.asarray(featuresMatrix.sum(axis=0)).ravel().tolist()})
word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
print word_freq_df.sort('occurrences',ascending = False).head(10)
#word_freq_df.to_csv('word_freq_medium.csv', encoding = 'UTF8')

  
#featuresMatrix.shape
#len(cv.vocabulary_)
#4) Get the vocabulary
voc = cv.vocabulary_
#5) Build a data frame from the fearue matrix using the vocabulary as the columns names
dfvoc = pd.DataFrame(featuresMatrix, index = df.index, columns = [i[0] for i in sorted(voc.items(), key=operator.itemgetter(1))])
 
#DEBUG:
#df.loc[0]['message']
#dfvoc.loc[0].to_clipboard()
 
df = df.join(dfvoc, how='left')



from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier(n_estimators=10)

predictors = [x for x in df.columns if x not in ['message']]
clf = clf.fit(df[predictors], df['status'])

preds = pd.DataFrame( 
                    clf.predict_proba(df[predictors])
                    ,index = df.index, columns = ['Prob_'+str(i) for i in clf.classes_])


preds = df.join(preds, how='left')
preds[['message', 'status', 'Prob_0']]