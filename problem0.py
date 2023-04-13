import nltk
# nltk.download('brown')
from nltk.corpus import brown

full_text = brown.words()

frequencies = nltk.FreqDist(word.lower() for word in full_text)

print(frequencies)

# print(frequencies.most_common(len(full_text)))

# include frequencies?
words_by_desc = frequencies.most_common(len(full_text))

adventure = brown.words(categories='adventure')
science_fiction = brown.words(categories='science_fiction')

print(science_fiction)