#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

import numpy as np
from generate import GENERATE


vocab = open("brown_vocab_100.txt")

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    #TODO: import part 1 code to build dictionary
    line = line.rstrip('\n')
    word_index_dict[line] = i

sentences = []
f = open("brown_100.txt")

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        lower.append(word.lower())
    sentences.append(lower[:-1])



# print(sentences)

#TODO: initialize counts to a zero vector
counts = np.zeros(813)

#TODO: iterate through file and update counts
for sentence in sentences:
    for word in sentence:
        counts[word_index_dict[word]] += 1


print(counts)



#TODO: normalize and writeout counts. 
probs = counts / np.sum(counts)

with open('unigram_probs.txt.txt', 'w') as f:
    for prob in probs:
        f.write("%s\n"%(str(prob)))


