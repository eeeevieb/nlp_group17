import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random
import math

#load data 
sentences = []
f = open("brown_100.txt")
vocab = open("brown_vocab_100.txt")

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")

    for word in line:
        lower.append(word.lower())
    sentences.append(lower[:-1])

#count words 
counts = {}
for sentence in sentences:
    for word in sentence:
        if word not in counts:
            counts[word]=0
        counts[word] +=1 

#select words that occur more than 10 times 
high_counts = {}

for word in counts:
    if counts[word] >= 10:
        high_counts[word] = counts[word]

#load the indices dictionary
word_index_dict = {}
for i, line in enumerate(vocab):
    line = line.rstrip('\n')
    word_index_dict[line] = i

pmis = {}
pair_counts = np.load("bigram_counts.npy")

# calculate pmis
for word in counts:
    for second_word in counts:
        C_wi_wj = pair_counts[word_index_dict[word], word_index_dict[second_word]]
        Cwi = counts[word]
        Cwj = counts[second_word]
        if C_wi_wj != 0:
            pmi = math.log((C_wi_wj * 813) / (Cwi * Cwj))
            pmis[word+second_word] = pmi

# sort pmis and select highest and lowest 20
sorted_pmis = dict(sorted(pmis.items(), key=lambda item: item[1]))

highest = list(sorted_pmis)[-20:]
lowest = list(sorted_pmis)[:20]

# write to txt file
with open('20_highset_pmis', 'w') as f:
    for pmi in highest:
        f.write("%s\n"%(str(pmi)))

with open('20_lowest_pmis', 'w') as f:
    for pmi in lowest:
        f.write("%s\n"%(str(pmi)))

