import os
from _collections import defaultdict
count = 0
labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
path_name = str("C:/Users/sai vishnu/workspace/NewCorrect/Multi")
f1 = open("C:/Users/sai vishnu/workspace/NewCorrect/predict_Comedy", "r", errors='ignore')
f2 = open("C:/Users/sai vishnu/workspace/NewCorrect/predict_Horror", "r", errors='ignore')
f3 = open("C:/Users/sai vishnu/workspace/NewCorrect/predict_Romance", "r", errors='ignore')
f4 = open("C:/Users/sai vishnu/workspace/NewCorrect/predict_Drama", "r", errors='ignore')
f5 = open("C:/Users/sai vishnu/workspace/NewCorrect/predict_Science_Fiction", "r", errors='ignore')
f6 = open("C:/Users/sai vishnu/workspace/NewCorrect/test_movie.txt", "r", errors='ignore')
labels_comedy = []
labels_drama = []
labels_romance = []
labels_horror= []
labels_science_fiction = []
films = []
import sys
correct = 0
for i in f1.readlines():
    file_names = {}
    j = i.split()
    labels_comedy.append(j[0])
for i in f2.readlines():
    file_names = {}
    j = i.split()
    labels_horror.append(j[0])
for i in f3.readlines():
    file_names = {}
    j = i.split()
    labels_romance.append(j[0])
for i in f4.readlines():
    file_names = {}
    j = i.split()
    labels_drama.append(j[0])
for i in f5.readlines():
    file_names = {}
    j = i.split()
    labels_science_fiction.append(j[0])

for j in f6.readlines():
    films.append(j)
           

film_dict = defaultdict(list)
for i in range(len(films)):
    temp_list = []
    if "0"==labels_comedy[i]:
        temp_list.append("Comedy")
    if "0"==labels_drama[i]:
        temp_list.append("Drama")
    if "0"==labels_romance[i]:
        temp_list.append("Romance")
    if "0"==labels_horror[i]:
        temp_list.append("Horror")
    if "0"==labels_science_fiction[i]:
        temp_list.append("Science_Fiction")
    film_dict[films[i]]=temp_list

total = 0

for i in films:
    print(i)
       
for k,v in film_dict.items():
    for labels in v:
        if labels in k:
            correct += 1
            break
    total += 1
print("Accuarcy: "+correct/total)
        
