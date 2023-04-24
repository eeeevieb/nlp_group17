import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random

#load data 
sentences = []
f = open("brown_100.txt")

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        lower.append(word.lower())
    sentences.append(lower[:-1])

#select words that occur more often then 10 times 
#count words 
counts = {}
for sentence in sentences:
    for word in sentence:
        if word not in counts:
            counts[word]=0
        counts[word] +=1 

print(counts)
