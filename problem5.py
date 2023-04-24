import numpy as np
from sklearn.preprocessing import normalize
from generate import GENERATE
import random

sentences = []
f = open("brown_100.txt")

for line in f:
    lower = []

    line = line.rstrip("\n")
    line = line.split(" ")
    for word in line:
        lower.append(word.lower())
    sentences.append(lower[:-1])


def trigram(findword, nextword, nextnextword, sentences):
    count_1 = 0 
    count_2 = 0
    for sentence in sentences:
        for count, word in enumerate(sentence):
            if word == findword:
                next_word = sentence[count+1]
                if next_word == nextword:
                    count_1 +=1 
                    next_2_word = sentence[count+2]
                    if next_2_word == nextnextword: 
                        count_2 +=1 
    return count_1,count_2




### 1
counts = trigram("in", "the", "past", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)

### 2
counts = trigram("in", "the", "time", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)

### 3
counts = trigram("the", "jury", "said", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)

### 4
counts = trigram("the", "jury", "recommended", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)

### 5
counts = trigram("the", "jury", "that", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)

### 6
counts = trigram("agriculture", "teacher", ",", sentences)
p_1 = counts[1]/counts[0]
print(p_1)
p_1_smooth = (counts[1]+0.1)/(counts[0]+0.1*813)
print(p_1_smooth)


