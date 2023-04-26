#!/usr/bin/env python3

"""
NLP A2: N-Gram Language Models

@author: Klinton Bicknell, Harry Eldridge, Nathan Schneider, Lucia Donatelli, Alexander Koller

DO NOT SHARE/DISTRIBUTE SOLUTIONS WITHOUT THE INSTRUCTOR'S PERMISSION
"""

word_index_dict = {}

# read brown_vocab_100.txt into word_index_dict
with open('brown_vocab_100.txt') as brown:
    lines = brown.readlines()

    for count, word in enumerate(lines):
        word = word.rstrip('\n')
        word_index_dict[word] = count
        

# write word_index_dict to word_to_index_100.txt
with open('word_to_index_100.txt', 'w') as f:
    for word in word_index_dict:
        f.write("%s,%s\n"%(word,str(word_index_dict[word])))

# check output
print(word_index_dict['all'])
print(word_index_dict['resolution'])
print(len(word_index_dict))
