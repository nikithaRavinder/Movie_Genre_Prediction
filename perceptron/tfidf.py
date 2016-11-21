from __future__ import division, unicode_literals
import math

idf_word = {}
n_dict = 0

def tf(word_c, total_words):
    return (word_c / total_words)


def idf(word, all_dict):
    global idf_word
    if word not in idf_word:
        n_containing = sum(1 for dict in all_dict if word in dict)
        idf_word[word] = math.log(n_dict / (1 + n_containing))
    return idf_word[word]

def tfidf(all_dict):
    x = {}
    global n_dict
    n_dict = len(all_dict)
    for key in all_dict.keys():
        total_words = sum(all_dict[key].values())
        x[key] = {}
        for word in all_dict[key]:
            x[key][word] = tf(all_dict[key][word], total_words) * idf(word, all_dict)
    return x