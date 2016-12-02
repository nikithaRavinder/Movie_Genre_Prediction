__author__ = "Megha Sharma"
import sys
import os
import json
import random
import tfidf
from stopwords import stopwords
import re

def strip_nonalnum_re(word):
    return re.sub(r"^\W+|\W+$", "", word)


x = {}
#dirname = "Genres"
dirname = "Data/Train"
#dirname = str(sys.argv[1])
words = []
for dirpath, dirs, files in os.walk(dirname):
    for filename in files:
        if filename[filename.rfind(".") + 1:] == "txt":
            i = filename
            x[i] = {}
            fname = os.path.join(dirpath, filename)
            f = open(fname, "r", encoding="latin1")
            text = f.read()
            f.close()
            tokens = text.split()
            for token in tokens:
                token = strip_nonalnum_re(token)
                if token.lower() in stopwords:
                    continue
                if token not in x[i]:
                    x[i][token] = 1
                else:
                    x[i][token] += 1
#print(str(x[5173]))
x, idf, sq = tfidf.tfidf(x)
model = {}
labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
for label in labels:
    b = 0
    ab = 0
    c = 1
    w = {}
    u = {}
    y = {}
    ITER = 30
    for j in range(0,ITER):
        num_label = 0
        num_non_label = 0
        for key, value in sorted(x.items(), key=lambda x: random.random()):
            if num_label > 700 and num_non_label > 700:
                break
            if label in key:
                if num_label > 700:
                    continue
                y[key] = 1
                num_label += 1
            else:
                if num_non_label > 700:
                    continue
                y[key] = -1
                num_non_label += 1
            a = b
            for token in value:
                if token not in w:
                    w[token] = 0
                    u[token] = 0
                a = a + value[token] * w[token]
            if y[key] * a <= 0:
                for token in value:
                    w[token] += y[key] * value[token]
                    u[token] += y[key] * value[token] * c
                b = b + y[key]
                ab = ab + y[key] * c
            c += 1
        print(str(num_non_label)+" "+str(num_label))
    for token in w:
        u[token] = w[token] - u[token]/c
    ab = b - ab/c
    model[label] = {
        "b":ab,
        "w":u
        }

wfile = open('per_model.txt', 'w+',encoding="latin1")
json.dump(model,wfile)
wfile.close()