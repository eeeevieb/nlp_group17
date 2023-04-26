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

counts = np.zeros((813,813)) # initialize numpy 0s array
print(counts)

# iterate through file and update counts
for sentence in sentences:
    previous_word = '<s>'
    for word in sentence[1:]: 
        #columns are ordering the previous words and rows are ordering the words 
        counts[word_index_dict[previous_word], word_index_dict[word]] += 1
        previous_word = word

# add smoothing to counts
counts += 0.1

# normalize counts
probs = normalize(counts, norm='l1', axis=1)

# writeout bigram probabilities
print("p(the | all) = " + str(probs[word_index_dict['all'], word_index_dict['the']]))
print("p(jury | the) = " +str(probs[word_index_dict['the'], word_index_dict['jury']]))
print("p(campaign | the) = " + str(probs[word_index_dict['the'], word_index_dict['campaign']]))
print("p(calls | anonymous) = " + str(probs[word_index_dict['anonymous'], word_index_dict['calls']]))
f.close()


# problem 6 - calculating perplexities

# load toy corpus
toy_sentences = []
f = open("toy_corpus.txt")

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        lower.append(word.lower())
    toy_sentences.append(lower[:-1])

# calculate sentence probability
sentprob = [1,1]

for count, sentence in enumerate(toy_sentences):
    previous_word = '<s>'
    for word in sentence[1:]: 
        #columns are ordering the previous words and rows are ordering the words 
        sentprob[count] *= probs[word_index_dict[previous_word], word_index_dict[word]]
        previous_word = word

# calculate perplexity of each sentence
sent_len = [len(toy_sentences[0]) - 1,len(toy_sentences[1]) - 1]

perplexity1 = 1/(pow(sentprob[0], 1.0/sent_len[0]))
perplexity2 = 1/(pow(sentprob[1], 1.0/sent_len[1]))

# write to txt file
with open('smoothed_eval.txt', 'w') as f:
    f.write("%s\n%s\n"%(str(perplexity1), str(perplexity2)))