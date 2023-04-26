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
    #import part 1 code to build dictionary
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

#initialize counts to a zero vector
counts = np.zeros(813)

#iterate through file and update counts
for sentence in sentences:
    for word in sentence:
        counts[word_index_dict[word]] += 1

#normalize and writeout counts. 
probs = counts / np.sum(counts)

with open('unigram_probs.txt', 'w') as f:
    for prob in probs:
        f.write("%s\n"%(str(prob)))


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

# calculate sentence probablities
sentprob = [1,1]

for count, sentence in enumerate(toy_sentences):
    for word in sentence:
       sentprob[count] *= probs[word_index_dict[word]]

# calculate perplexities
sent_len = [len(toy_sentences[0]),len(toy_sentences[1])]

perplexity1 = 1/(pow(sentprob[0], 1.0/sent_len[0]))
perplexity2 = 1/(pow(sentprob[1], 1.0/sent_len[1]))

# write to txt file
with open('unigram_eval.txt', 'w') as f:
    f.write("%s\n%s\n"%(str(perplexity1), str(perplexity2)))

