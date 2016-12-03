import os
import sys
from _collections import defaultdict
count = 0
labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
path_name = str("C:/Users/sai vishnu/workspace/NewCorrect/Multi")
f1 = open("predict_Comedy", "r", errors='ignore')
f2 = open("predict_Horror", "r", errors='ignore')
f3 = open("predict_Romance", "r", errors='ignore')
f4 = open("predict_Drama", "r", errors='ignore')
f5 = open("predict_Science_Fiction", "r", errors='ignore')

labels_comedy = []
labels_drama = []
labels_romance = []
labels_horror= []
labels_science_fiction = []

def Calculate(label, fileObj):
    
    f6 = sys.argv[1] # path to the file which has all the movie names  
    labels = []
    films = []
    rel = 0.0
    tot_rel = 0.0 
    ret = 0.0
    correct = 0.0
    for i in fileObj.readlines():
        file_names = {}
        j = i.split()
        labels.append(j[0])
    for j in f6.readlines():
        films.append(j)
    print(label+": ")
   
    for i in range(len(films)):
        if(labels[i]=='0' and label in films[i]):
            rel += 1
        ret += 1
        if(label in films[i]):
            tot_rel += 1
 
    precision = rel/ret
    recall = rel/tot_rel
    f1Score = (2*precision*recall)/(precision+recall)
    print ("Precision: "+ str(precision*100))
    print("Recall: "+ str(recall*100))
    print("F-Score: "+ str(f1Score*100))
    f6.close()


Calculate("Comedy", f1, )
Calculate("Horror", f2)
Calculate("Romance", f3)
Calculate("Drama", f4)
Calculate("Science_Fiction", f5)
 
        