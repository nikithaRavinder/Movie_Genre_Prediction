__author__ = "Megha Sharma"
from __future__ import division
import os
import tfidf
import math
import operator
from stopwords import stopwords
import re

def strip_nonalnum_re(word):
    return re.sub(r"^\W+|\W+$", "", word)

x = {}
idf = {}
sq = {}

labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
#labels = ["ham", "spam"]

def preprocess():
    #dirname = "Genres"
    dirname = "Data/Train"
    #dirname = str(sys.argv[1])
    #dirname = "C:/Users/Megha/Documents/studies/544/HW1/project/SpamorHam/train"
    global labels, x, sq, idf
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
    x, idf, sq = tfidf.tfidf(x)

def weight(d):
    global idf, x, sq
    total_words = sum(d.values())
    dsq = 0
    d1 = {}
    for word in d:
        if word in idf:
            d1[word] = tfidf.tf(d[word], total_words) * idf[word]
            dsq += d1[word] * d1[word]
    return d1, dsq

def cdistance(d, dsq, file):
    global idf, x, sq
    denom = 0.000001
    for word in d:
        if word in x[file]:
            denom += x[file][word] * d[word]
    num = math.sqrt(sq[file]) * math.sqrt(dsq)
    dis = num / denom
    return dis

def distance(d, file, total_words):
    global idf, x, sq
    num = 0
    flag = 0.000001
    for word in d:
        if word in x[file]:
            flag += 1
            num += (x[file][word] - d[word]) * (x[file][word] - d[word])
    #print(file + str(flag))
    if num == 0:
        num = total_words / flag
    else:
        num = num * total_words / flag
    if flag <= 5:
        dis = 999999
    else:
        dis = math.sqrt(num)
    return dis

def getResponse(d, k):
    global x, labels
    distances = {}
    total_words  = len(d)
    d, dsq = weight(d)
    for file in x.keys():
        dist = cdistance(d, dsq, file)
        #dist = distance(d, file, total_words)
        distances[file] = dist
    distances = sorted(distances.items(), key=operator.itemgetter(1))
    i = 0
    classVotes = {}
    for file in distances:
        neighbor = file[0]
        print(neighbor + str(file[1]))
        for label in labels:
            if label in neighbor:
                response = label
                if response in classVotes:
                    classVotes[response] += 1
                else:
                    classVotes[response] = 1
        i += 1
        if i > k:
            break
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    res = []
    i = 0
    for k in sortedVotes:
        res.append(k[0])
    return res



def main():
    # prepare data
    global labels
    st = ""
    res = {}
    for label in labels:
        res[label] = [[0, 0], [0, 0]]
    # dirname = str(sys.argv[1])
    #print(dirname)
    dirname = "Test"
    #dirname = "C:/Users/Megha/Documents/studies/544/HW1/project/SpamorHam/dev"
    #dirname = "Data/Test"
    preprocess()
    for dirpath, dirs, files in os.walk(dirname):
        for filename in files:
            if filename[filename.rfind(".") + 1:] == "txt":
                d = {}
                fname = os.path.join(dirpath, filename)
                f = open(fname, "r", encoding="latin1")
                text = f.read()
                f.close()
                tokens = text.split()
                for token in tokens:
                    token = strip_nonalnum_re(token)
                    if token.lower() in stopwords:
                        continue
                    if token not in d:
                        d[token] = 1
                    else:
                        d[token] += 1
                k = 6
                result = getResponse(d, k)


                actual_set = set()
                for label in labels:
                    if label in fname:
                        actual_set.add(label)
                result_set = set(result[0:min(len(result), len(actual_set))])
                print(filename + " - res: " + str(result_set)+ " - actual: "+ str(actual_set))
                for label in actual_set.intersection(result_set):
                    res[label][0][0] += 1
                for label in result_set - actual_set:
                    res[label][1][0] += 1
                for label in actual_set - result_set:
                    res[label][0][1] += 1

    for label in labels:
        hprec = res[label][0][0] / (res[label][0][0] + res[label][1][0])
        hrec = res[label][0][0] / (res[label][0][0] + res[label][0][1])
        hfsc = 2 * hprec * hrec / (hprec + hrec)
        print("\n" + label + "\nprecision: " + str(hprec) + "\nrecall: " + str(hrec) + "\nscore: " + str(
            hfsc))




main()