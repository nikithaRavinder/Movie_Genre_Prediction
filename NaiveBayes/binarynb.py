__author__ = "Nikitha Ravinder"

import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
stop = stopwords.words("english")

labels = ["Romance", "Comedy", "Drama", "Horror", "Science_Fiction"]
file_dict = {}
total_files_count = 0
train_path = str("/Users/nikitha/Desktop/USC/4.Fall2016/NLP/FinalProject/DataF/Train")
for label in labels:
    file_dict[label] = []
    file_dict["not_"+label] = []
for root, dirs, files in os.walk(train_path):
    for file in files:
        if file.endswith(".txt"):
            for label_name in labels:
                if label_name in file:
                    file_dict[label_name].append(os.path.join(root, file))
                else:
                    file_dict["not_"+label_name].append(os.path.join(root, file))
                total_files_count += 1

train_data = []
label_list = []
for label in labels:
    not_label = "not_" + label
    for file in file_dict[label]:
        with open(file, "r") as f:
            plot = f.read()
            train_data.append(plot)
            label_list.append(label)
    for file in file_dict[not_label]:
        with open(file, "r") as f:
            plot = f.read()
            train_data.append(plot)
            label_list.append(not_label)
label_data = list(zip(train_data, label_list))

count_vect = CountVectorizer(ngram_range=(1, 3))
tfidf = TfidfTransformer()
stemmer = PorterStemmer()
stem_train_data = []
for plot in train_data:
    words_in_doc = " ".join([stemmer.stem(w) for w in plot.split() if w not in stop])
    stem_train_data.append(words_in_doc)
X_train_counts = count_vect.fit_transform(stem_train_data)
X_train_tfidf = tfidf.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_counts, label_list)

test_path = str("/Users/nikitha/Desktop/USC/4.Fall2016/NLP/FinalProject/DataF/Test")
test_files = []
test_data = []
for root, dirs, files in os.walk(test_path):
    for file in files:
        if file.endswith(".txt"):
            test_files.append(os.path.join(root, file))
            with open(os.path.join(root, file), "r") as f:
                plot = f.read()
                test_data.append(plot)
stem_test_data = []
for plot in test_data:
    words_in_doc = " ".join([stemmer.stem(w) for w in plot.split() if w not in stop])
    stem_test_data.append(words_in_doc)

X_test_counts = count_vect.transform(stem_test_data)
X_test_tfidf = tfidf.fit_transform(X_test_counts)

predicted_prob = clf.predict_proba(X_test_counts)
probs = predicted_prob.tolist()
with open("output.txt", "w+") as op:
    for doc, prob in zip(test_files, probs):
        res_values = {}
        result = []
        #print(doc, [(x, y) for x, y in zip(prob, clf.classes_)])
        for x,y in zip(prob, clf.classes_):
            res_values[y] = x
        #print(res_values)
        for label in labels:
            not_label = "not_"+label
            if res_values[label] >= res_values[not_label]:
                result.append(label)
            #else:
                #result.append(not_label)
        #print(result)

        op.write("" + doc[doc.rfind("/")+1:] + "\t" + str(result) + "\n")





