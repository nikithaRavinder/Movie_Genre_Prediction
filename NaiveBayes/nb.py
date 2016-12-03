__author__ = "Nikitha Ravinder"

import os
from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stop = stopwords.words("english")

count_vect = CountVectorizer(ngram_range=(1, 3))
tfidf = TfidfTransformer()
stemmer = PorterStemmer()


def nbtrain(type):
    global train_data, count_vect, tfidf, stemmer
    Y = train_data.target
    X_train_counts = count_vect.fit_transform(train_data.data)
    X_train_tfidf = tfidf.fit_transform(X_train_counts)
    if type == "wordcount":
        X_train = X_train_counts
    elif type == "tfidf":
        X_train = X_train_tfidf

    clf = MultinomialNB().fit(X_train, Y)
    return clf


def nbtest(type, clf):
    global count_vect, test, stemmer
    X_test_counts = count_vect.transform(test[1])
    if type == "wordcount":
        X_test = X_test_counts
    elif type == "tfidf":
        X_test_tfidf = tfidf.transform(X_test_counts)
        X_test = X_test_tfidf

    predicted_prob = clf.predict_proba(X_test)
    tags = list(set(train_data.target.tolist()))
    probs = predicted_prob.tolist()
    with open("output.txt", "w+") as op:
        for doc, prob in zip(test[0], probs):
            op.write("" + doc[doc.rfind("/")+1:] + "\t" + str(
                [train_data.target_names[y] for x, y in zip(prob, tags) if x >= 0.2]) + "\n")



categories = ['Romance', 'Drama', 'Science_Fiction', 'Comedy', 'Horror']
train_path = "/Users/nikitha/Desktop/USC/4.Fall2016/NLP/FinalProject/DataF/Train"
train_data = load_files(train_path, description=None, categories=categories, load_content=True, shuffle=True, encoding="latin1", decode_error='strict', random_state=0)
new_train_data = []
for line in train_data.data:
    words_in_doc = " ".join([stemmer.stem(w) for w in line.split() if w not in stop])
    new_train_data.append(words_in_doc)


test_path = "/Users/nikitha/Desktop/USC/4.Fall2016/NLP/FinalProject/DataF/Test"
test = []
test_data = []
test_file = []
for root, dirs, files in os.walk(test_path):
    for file in files:
        if file.endswith(".txt"):
            test_file.append(os.path.join(root, file))
            with open(os.path.join(root, file), "r", encoding="latin1") as f:
                plot = f.read()
                test_data.append(plot)

test.append(test_file)
test.append(test_data)
new_test_data = []
for plot in test[1]:
    words_in_doc = " ".join([stemmer.stem(w) for w in plot.split() if w not in stop])
    new_test_data.append(words_in_doc)

"""Stemming"""
X_train_counts = count_vect.fit_transform(new_train_data)
clf = MultinomialNB().fit(X_train_counts, train_data.target)
X_test_counts = count_vect.transform(new_test_data)
pred = clf.predict_proba(X_test_counts)
probs = pred.tolist()
with open("output.txt", "w+") as op:
    for doc, prob in zip(test[0], probs):
        op.write("" + doc[doc.rfind("/"):] + "\t" + str(
            [train_data.target_names[y] for x, y in zip(prob, list(set(train_data.target.tolist()))) if x >= 0.2]) + "\n")

"""
clf = nbtrain("tfidf")
nbtest("tfidf", clf)
"""



