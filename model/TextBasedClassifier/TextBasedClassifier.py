import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
import operator
from sklearn.metrics import log_loss
from sklearn.utils import shuffle
import os 
from sklearn.ensemble import RandomForestClassifier
import pickle

class TextBasedClassifier():
    
    def __init__(self):
        self.MODEL = None
        self.MODEL_FEATURES = ''
        self.DATA_FILE_LOCATION = os.path.join( (os.path.dirname(os.path.realpath('__file__'))), 'model', 'TextBasedClassifier')
    
    
    def _readTrainData(self):
    
        ################################### READ TRAINING DATA
        #df = pd.DataFrame([
        #                    ['Hello how are you?',0], 
        #                    ['feck off you idiot',1],
        #                    ['I AM NOT DRUNK',1]
        #                    ], columns=['message', 'status'])
        
        df = pd.read_table(os.path.join(self.DATA_FILE_LOCATION, 'drunk.txt'))
        df.columns = ['message']
        df['status']=1
          
        dfnot = pd.read_table(os.path.join(self.DATA_FILE_LOCATION, 'not_drunk.txt'))
        dfnot.columns = ['message']
        dfnot['status']=0
        
        df = pd.concat([df, dfnot], axis=0)
        df = shuffle(df)
        
        return df
    
    def _cleanUpDataFrame(self, df):
        ####################################### VERY SILLY DATA CLEAN UP
        
        def cleanString(_str):
            ret=''
            for i in _str.split():
                if len(i)<3:
                    continue
                if i.startswith('u'):            
                    continue
                if i.startswith('@'):            
                    continue
                if i.startswith('#'):
                    continue          
                ret +=' '+ i.strip()
            return ret
            
        
        df = df.loc[~df['message'].str.startswith('RT')]
        
        df['message'] = df['message'].apply(lambda x : ''.join([i for i in x if not i.isdigit()]))
        df['message'] = df['message'].apply(lambda x : x.replace('message', '' ))
        df['message'] = df['message'].apply(lambda x : x.replace('\\', ' ' ))
        df['message'] = df['message'].apply(lambda x : cleanString(x))
        
        return df
    
    
    def _prepareTrainingData(self, df):
        
        ################################### PREPARE TRAINING DATA
        #2)Create and fit the CountVectorizer
        cv = CountVectorizer(stop_words='english', min_df=3, max_features=400) #vocabulary=['hot', 'cold', 'old'] 
        
        #3)Get the geature Matrix
        featuresMatrix = cv.fit_transform(df["message"]).toarray()
        #featuresMatrix = cv.fit_transform(dfall[dfall['interest_level'] == 'medium']["features2"]).toarray()
         
         
        word_freq_df = pd.DataFrame({'term': cv.get_feature_names(), 'occurrences':np.asarray(featuresMatrix.sum(axis=0)).ravel().tolist()})
        word_freq_df['frequency'] = word_freq_df['occurrences']/np.sum(word_freq_df['occurrences'])
        #print word_freq_df.sort('occurrences',ascending = False).head(30)
        #word_freq_df.to_csv('word_freq_medium.csv', encoding = 'UTF8')
        #word_freq_df.to_clipboard()
          
        #featuresMatrix.shape
        #len(cv.vocabulary_)
        #4) Get the vocabulary
        voc = cv.vocabulary_
        #5) Build a data frame from the fearue matrix using the vocabulary as the columns names
        dfvoc = pd.DataFrame(featuresMatrix, index = df.index, columns = [i[0] for i in sorted(voc.items(), key=operator.itemgetter(1))])
         
        self.MODEL_FEATURES = dfvoc.columns
        #DEBUG:
        #df.loc[100]['message']
        #dfvoc.loc[100].to_clipboard()
         
        df = df.join(dfvoc, how='left')
        return df
    
    def _trainModel(self, df):    
        self.MODEL = RandomForestClassifier(n_estimators=2000)
        
        predictors = [x for x in df.columns if x not in ['message', 'status']]
        self.MODEL.fit(df[predictors], df['status'])
        
        
        
    def TrainTextBasedClassifier(self):
        
        df = self._readTrainData()
        df = self._cleanUpDataFrame(df)
        df = self._prepareTrainingData(df)
        self._trainModel(df)
        
        pickle.dump((self.MODEL, self.MODEL_FEATURES), open(os.path.join( self.DATA_FILE_LOCATION, 'TextBasedClassifier_MODEL'), 'wb'))
        

    def Predict(self, text):
        try:
            model = pickle.load(open(os.path.join(self.DATA_FILE_LOCATION, 'TextBasedClassifier_MODEL'), 'rb')) 
        except:
            raise Exception("Text Based Model is not trained")
        
        if self.MODEL is None:
            print 'loading model'
            self.MODEL = model[0] 
            self.MODEL_FEATURES = model [1]

        cv = CountVectorizer(stop_words='english', max_features=400)
        featuresMatrix = cv.fit_transform([text]).toarray()
        voc = cv.vocabulary_
        dfpred = pd.DataFrame(featuresMatrix, columns = [i[0] for i in sorted(voc.items(), key=operator.itemgetter(1))])
    
        #removes the new features the model is not aware of
        dfpred.drop([x for x in dfpred.columns if x not in self.MODEL_FEATURES], axis =1, inplace=True)
        
        #ad the missing features the model expect but the testing data doesnt have
        for col in [i for i in self.MODEL_FEATURES if i not in dfpred.columns]:
            dfpred[col]=0
                  
        dfpred = dfpred[self.MODEL_FEATURES]
        return pd.DataFrame(self.MODEL.predict_proba(dfpred) ,index = dfpred.index, columns = ['Prob_'+str(i) for i in self.MODEL.classes_])


#    
#    #############################TEST WITH TRAINING DATA (OVERFITING)
#    
#    preds = pd.DataFrame( 
#                        MODEL.predict_proba(df[predictors])
#                        ,index = df.index, columns = ['Prob_'+str(i) for i in MODEL.classes_])
#    
#    
#    preds = df.join(preds, how='left')
#    preds[['message', 'status', 'Prob_0', 'Prob_1']]
#    
#    log_loss(preds[['status']], preds[['Prob_0', 'Prob_1']])
#    
#    
#    
#    
#    #############################TEST WITH NEW DATA
#    
#    
#    
#    
#    predict('drunk as hell')
#    predict('hey buddy, how are you today?')
#    predict('hello')