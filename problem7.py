import generate
import problem2
import problem3
import problem4
f1 = open("unigram_generation.txt", "w")
f2 = open("bigram_generation.txt", "w")
f3 = open("smoothed_generation.txt", "w")
for _ in range(10):
    f1.write(generate.GENERATE(problem2.word_index_dict, problem2.probs, 'unigram', max_words=20, start_word=""))
    f1.write("\n")
    f2.write(generate.GENERATE(problem3.word_index_dict, problem3.probs, 'bigram', max_words=20, start_word="<s>"))
    f2.write("\n")
    f3.write(generate.GENERATE(problem4.word_index_dict, problem4.probs, 'bigram', max_words=20, start_word="<s>"))
    f3.write("\n")

f1.close()
f2.close()
f3.close()