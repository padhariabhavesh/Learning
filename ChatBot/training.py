# import dependencies

import random
import json
import pickle
import numpy as np
import nltk
nltk.download('omw-1.4')
import warnings
warnings.filterwarnings('ignore')
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLemmatizer
intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.append(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
print(documents)
print('*'* 30)


wnl = WordNetLemmatizer()

lemmatized_words = [[wnl.lemmatize(word) for word in l] for l in words]
print(lemmatized_words)
print('*'* 30)

classes = sorted(set(classes))
pickle.dump(words, open('lemmatized_words.pkl', 'wb'))
pickle.dump(words, open('classess.pkl', 'wb'))

# training = []
# output_empty = [0] * len(classes)
