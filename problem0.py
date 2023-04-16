import nltk
# nltk.download('brown')
import matplotlib.pyplot as plt
import numpy as np

brown = nltk.corpus.brown

# Compute a list of unique words sorted by descending frequency for (i) the whole corpus
# and (ii) two different genres of your choice.

# should we pre-process, e.g. to filter all non-words such as full stops and spaces?

brown_words = brown.words()

FD_brown = nltk.FreqDist(word.lower() for word in brown_words)
FD_adv = nltk.FreqDist(word.lower() for word in brown.words(categories='adventure'))
FD_scifi = nltk.FreqDist(word.lower() for word in brown.words(categories='science_fiction'))

sorted_words_brown = sorted(set(brown_words), key=lambda w: -FD_brown[w])
# print("Ten most frequent words from Brown: "+str(sorted_words_brown[:10]))
sorted_words_adv = sorted(set(brown.words(categories='adventure')), key=lambda w: -FD_adv[w])
# print("Ten most frequent words from Adventure genre: "+str(sorted_words_adv[:10]))
sorted_words_scifi = sorted(set(brown.words(categories='science_fiction')), key=lambda w: -FD_scifi[w])
# print("Ten most frequent words from Science fiction genre: "+str(sorted_words_scifi[:10]))

# extract the following information (should be visible in your code and output files): number of tokens;
# number of types; number of words; average number of words per sentence; average word length.
print("Number of tokens: "+str(len(brown_words))) # Is the number of tokens different from the number of words?
print("Number of types: "+str(len(set(brown_words))))
print("Number of words: "+str(len(brown_words)))
# average number of words per sentence = total number of words / number of sentences
brown_sentences = brown.sents()
print("Average number of words per sentence: "+str(len(brown_words)/len(brown_sentences)))
# average word length = total number of characters / number of words
brown_chars = brown.raw()
print("Average word length: "+ str(len(brown_chars)/len(brown_words)))

#  You should also run a default part-of-speech tagger on the dataset and identify the ten most frequent POS tags.
freq_POS = nltk.FreqDist(tag[1] for tag in brown.tagged_words())
print("Ten most frequent POS tags: "+str(freq_POS.most_common(10)))

# Next, Use the Python library matplotlib to plot the frequency curves for the corpus and two genres you choose:
# i.e. x-axis is position in the frequency list, y-axis is frequency.
# Provide both a plot with linear axes and one with log-log axes.

fig, axs = plt.subplots(3, 2)
results = [FD_brown, FD_adv, FD_scifi]
names = {0: 'Brown', 1: 'Genre adventure', 2: 'Genre science fiction'}

j = 0
for freq in results:
    ranks = range(len(freq))
    freqs = freq.values()
    log_freqs = log_ranks = np.zeros(len(freq))
    i = 0
    for value in freqs:
        log_freqs[i]=np.log(value)
        log_ranks[i] = np.log(i+1)
        i = i + 1

    axs[j][0].plot(ranks, freqs)
    axs[j][0].set_xlabel('Rank')
    axs[j][0].set_ylabel('Frequency')
    axs[j][0].set_title(f"Frequency Curve for \n {names[j]} (Linear)".format(**names))
    axs[j][1].plot(log_ranks, log_freqs)
    axs[j][1].set_xlabel('Log Rank')
    axs[j][1].set_ylabel('Log Frequency')
    axs[j][1].set_title(f"Frequency Curve for \n {names[j]} (Log-log)".format(**names))
    j = j + 1
plt.show()