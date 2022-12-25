#!/usr/bin/env python
# coding: utf-8

# Use the following google drive link incase code is not running in your local envionment
# https://drive.google.com/file/d/10WFbJYJ5-bGeeItmgGEFkin_Iy95jgP3/view?usp=sharing

# In[ ]:


import pandas as pd
import numpy as np
from nltk.stem import PorterStemmer
import re


# In[ ]:


class preprocessing():

    def __init__(self, filename):
        self.name = filename
        self.df = pd.read_csv(filename+".csv")
    
    def get_dataframe(self):
        return self.df

    def display(self):
        display(self.df.head())
        
    #Removing unicode characters (eg: //u2fed)
    def remove_unicode(self):
        count = 0
        string = ''
        for index,line in enumerate(self.df['text']):
            if '\\u' in line:
                line = line.replace('\\u',' #')
                token = line.split()
                count+=1
                for word in token:
                    if '#' not in word:
                        string += word + ' '
                self.df['text'][index] = string
                string = ''
        print("_____________________","Removed Unicode","________________________")
                
    #Converting to Lowercase
    def lowercase(self):
        self.df['text'] = self.df['text'].str.lower()
        print("_____________________","All text are lowercased","________________________")
        
    #Negation Words
    def negation_words(self):
        negated_dictionary = {'don\'t':"do not",'didn\'t': "did not",'can\'t':"cannot",'wouldn\'t':"would not",'doesn\'t':"does not",'i\'m':'i am'}
        #confusing_dictionary = {'vote out':'loser','out of office':'loser','vote him out':'loser'}
        for index,comments in enumerate(self.df['text']):
            text=""
            py_stem = PorterStemmer()
            token = comments.split()
            for word_index,word in enumerate(token):
                if word in negated_dictionary.keys():
                    token[word_index] = negated_dictionary[word]
                stemmed_word = py_stem.stem(word)
                if word_index+2 < len(token) and stemmed_word == "vote" and token[word_index+1] == "him" and token[word_index+2] == "out":
                    token.remove("him")
                    token.remove("out")
                    token[word_index] = "loser"
                if word_index+2 < len(token) and token[word_index] == "out" and token[word_index+1] == "of" and token[word_index+2] == "office":
                    token.remove("of")
                    token.remove("office")
                    token[word_index] = "loser"
                if word_index+1 < len(token)and stemmed_word == "vote" and token[word_index+1] == "out":
                    token.remove("out")
                    token[word_index] = "loser"
                text = " ".join(token)
            self.df['text'][index] = text
        print("_____________________","Expanded Negated words","________________________")
        
    #Applying Filter Rules
    def filter_rules(self):

        for index,line in enumerate(self.df['text']):
            line = line.replace("\\n","") # Replacing New Lines
            line = re.sub('http://\S+|https://\S+', '', line)  #Replacing URLS
            #line = re.sub('\S*@\S*\s?','',line)   #Replacing emails
            line = re.sub('\([^)]*\)','',line) #Replacing (strings)
            #line = re.sub('[^a-z]+',' ',line) #Replacing alphanumeric characters
            self.df['text'][index] = line
            
        print("_____________________","Applied Filter rules","________________________")
    
    def save_csv(self,string):
        self.df.to_csv("Output/{}_{}.csv".format(string,self.name[-3:]))
        print("_____________________","File saved","________________________")
        



