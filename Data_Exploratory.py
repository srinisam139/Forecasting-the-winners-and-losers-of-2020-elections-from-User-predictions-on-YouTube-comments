#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import nltk
from nltk.stem import PorterStemmer
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords
sw_nltk = stopwords.words('english')
import plotly.express as px
from nltk.tokenize import word_tokenize
import re
from collections import Counter
from nltk.util import ngrams


# In[ ]:


class data_exploratory:
    
    def __init__(self, filename):
        self.name = filename
        self.df = pd.read_csv(filename+".csv")
        self.pre_df = pd.DataFrame()
        self.post_df = pd.DataFrame()
    
    def get_dataframe(self):
        return self.df
    
    def display(self):
        display(self.df.head())
        
    #Calculating the avg, highest, lowest length from the entire corpus
    def count_words(self, df):
        highest_word_count = 0
        lowest_word_count = 1000
        length = 0
        total = 0
        doc_length = []
        for index,line in enumerate(df['text']):
            length = len(line)
            if length > highest_word_count:
                highest_word_count = length
            elif length < lowest_word_count:
                lowest_word_count = length
            total+=length
            doc_length.append(length)
        print("Highest Word Count:",highest_word_count)
        print("Lowest Word Count:",lowest_word_count)
        print("Average Word Count:",total/len(self.df))
        
    
    def bigram_trigram(self, df):
        bigram_list = []
        doc = []
        py_stem = PorterStemmer ()
        for comments in df['text']:
            tokens = [py_stem.stem(word) for word in comments.split()]
            for w in tokens: 
                if not w in sw_nltk:
                    doc.append(w)
        # get bigrams
        _2gram = ['_'.join(e) for e in ngrams(doc, 2)]
        _3gram = ['_'.join(e) for e in ngrams(doc, 3)]
        bigram_count = Counter(_3gram)
        print(bigram_count.most_common(20))
    
    #Function to count the keywords from the entire corpus
    def count_keywords(self,df):

        freq_df = df.copy()
        freq_df['text'] = freq_df['text'].str.lower()
        text = ' '.join(freq_df.text)
        py_stem = PorterStemmer ()
        token = [py_stem.stem(word) for word in text.split()]
        keywords = ['joe', 'biden', 'donald', 'won', 'trump', 'winner', 'win', 'vote','donaldtrump','joebiden']
        freq = {}
        for item in keywords:
            freq[item] = token.count(item)
        freq_df = pd.DataFrame(list(freq.items()), columns = ['keywords','count'])
        print(freq_df)
        fig = px.bar(freq_df, x='keywords', y='count')
        fig.show('notebook')
        
    
    #Filtering 15 days of data before the election day (2020-10-19 - 2020-11-02)
    def pre_election(self,count_bool = False):
        self.pre_df = self.df[self.df['timeline'] < '2020-11-03']
        if count_bool:
            self.count_keywords(self.pre_df)
            self.count_words(self.pre_df)

    #Filtering 5 days from the election date (2020-11-03 - 2020-11-07)
    def post_election(self, count_bool = False):
        self.post_df = self.df[self.df['timeline'] >= '2020-11-03']
        if count_bool:
            self.count_keywords(self.post_df)
            self.count_words(self.post_df)
            
    # Document is trimmed according to the data exploratory analysis to plus or minus k words 
    # around anchor words (eg:-20 words,'vote', +20 words)
    def trim_document(self,n):
        
        for index,value in enumerate(self.pre_df['text']):
            minus_string = ''
            positive_string = ''
            value = word_tokenize(value)
            #print(len(value))
            #print(value)
            if len(value) > n*2:
                py_stem = PorterStemmer ()
                token = [py_stem.stem(word) for word in value]
                token_index = 0
                for word in token:
                    if word in ['vote','win','won','winner']:
                        token_index = token.index(word)
                    if token_index <=n:
                        minus_ngram = value[:token_index]
                    else:
                        minus_ngram = value[token_index-n:token_index]
                    if len(token) > token_index+n:
                        positive_ngram = value[token_index:token_index+n]
                    else:
                        positive_ngram = value[token_index:len(token)]
                minus_string = ' '.join(minus_ngram)
                positive_string = ' '.join(positive_ngram)
                self.pre_df['text'][index] = minus_string + " "+ positive_string
        self.pre_df.to_csv("Output/trimmed_pre_election_punctuation_CNN_{}.csv".format(n))
