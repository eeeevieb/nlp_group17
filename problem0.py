import nltk
# nltk.download('brown')
import matplotlib.pyplot as plt
from collections import Counter


brown = nltk.corpus.brown

# Compute a list of unique words sorted by descending frequency for (i) the whole corpus
# and (ii) two different genres of your choice.
FD_brown = nltk.FreqDist(word.lower() for word in brown.words())
FD_adv = nltk.FreqDist(word.lower() for word in brown.words(categories='adventure'))
FD_scifi = nltk.FreqDist(word.lower() for word in brown.words(categories='science_fiction'))

sorted_words_brown = sorted(set(brown.words()), key=lambda w: -FD_brown[w])
print("Ten most frequent words from Brown: "+str(sorted_words_brown[:10]))
sorted_words_adv = sorted(set(brown.words(categories='adventure')), key=lambda w: -FD_adv[w])
print("Ten most frequent words from Adventure genre: "+str(sorted_words_adv[:10]))
sorted_words_scifi = sorted(set(brown.words(categories='science_fiction')), key=lambda w: -FD_scifi[w])
print("Ten most frequent words from Science fiction genre: "+str(sorted_words_scifi[:10]))

print("Words in position 500-510 Brown: "+str(sorted_words_brown[500:510]))
print("Words in position 500-510 Adventure genre: "+str(sorted_words_adv[500:510]))
print("Words in position 500-510 Science fiction genre: "+str(sorted_words_scifi[500:510]))

tokens = brown.words()
print("Number of tokens: "+str(len(tokens)))

types = set(tokens)
print("Number of types: "+str(len(types)))

# We count the number of distinct words as all types that are not punctuation. We treat a contraction (such as we'll)
# as 1 word, we treat numbers, dates, times, monetary amounts, acronyms and abbreviations all as words.
words = types
punctuation = ['.',',','?','!',':',';','\'','-','+','[',']','&','(',')','/']
for p in punctuation:
    words.remove(p)
print("Number of words: "+str(len(words)))

# average number of words per sentence = total number of words (here: tokens) / number of sentences
brown_sentences = brown.sents()
print("Average number of words per sentence: "+str(len(tokens)/len(brown_sentences)))

# average word length = total number of characters / number of words (here: tokens)
brown_chars = brown.raw()
print("Average word length: "+ str(len(brown_chars)/len(tokens)))

# default POS tagger
freq_POS_brown = nltk.FreqDist(tag[1] for tag in brown.tagged_words())
print("Ten most frequent POS tags Brown: "+str(freq_POS_brown.most_common(10)))
freq_POS_adv = nltk.FreqDist(tag[1] for tag in brown.tagged_words(categories="adventure"))
print("Ten most frequent POS tags Adventure: "+str(freq_POS_adv.most_common(10)))
freq_POS_scifi = nltk.FreqDist(tag[1] for tag in brown.tagged_words(categories="science_fiction"))
print("Ten most frequent POS tags Science Fiction: "+str(freq_POS_scifi.most_common(10)))

# Plot the frequency curves for the corpus and two genres
fig, axs = plt.subplots(1, 2)
results = {'Brown': FD_brown, 'Adventure': FD_adv, 'Science fiction': FD_scifi}

for res in results.keys():
    freq=results[res]
    ranks = range(1, len(freq)+1)
    freqs = [x[1] for x in freq.most_common()]

    axs[0].plot(ranks, freqs, label=res)
    axs[0].set_xlabel('Rank')
    axs[0].set_ylabel('Frequency')
    axs[0].set_title(f"Frequency Curve (Linear)")

    axs[1].plot(ranks, freqs, label=res)
    axs[1].set_xscale("log")
    axs[1].set_yscale("log")
    axs[1].set_xlabel('Log Rank')
    axs[1].set_ylabel('Log Frequency')
    axs[1].set_title(f"Frequency Curve (Log-log)")

plt.savefig('frequency_curves.png')
plt.legend()
plt.show()