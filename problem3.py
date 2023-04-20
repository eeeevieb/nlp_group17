#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random
vocab = open("brown_vocab_100.txt")
#vocab = codecs.open("brown_vocab_100.txt"), dit werkte niet. Zag die andere bij eva dus heb dat gedaan??? 

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
    line = line.rstrip('\n')
    word_index_dict[line] = i

sentences = []
f = open("brown_100.txt")
#f = codecs.open("brown_100.txt"), same as above with the vocab

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        lower.append(word.lower())
    sentences.append(lower[:-1])

#print(sentences)

counts = np.zeros((813,813)) #TODO: initialize numpy 0s array
print(counts)

#TODO: iterate through file and update counts
for sentence in sentences:
    previous_word = '<s>'
    for word in sentence[1:]: 
        #columns are ordering the previous words and rows are ordering the words 
        #look at  this maybe  it need to be otherway arround 
        print
        counts[word_index_dict[previous_word], word_index_dict[word]] += 1
        previous_word = word

#TODO: normalize counts
probs = normalize(counts, norm='l1', axis=1)

#TODO: writeout bigram probabilities
print(probs[word_index_dict['all'], word_index_dict['the']])
print(probs[word_index_dict['the'], word_index_dict['jury']])
print(probs[word_index_dict['the'], word_index_dict['campaign']])
print(probs[word_index_dict['anonymous'], word_index_dict['calls']])
f.close()