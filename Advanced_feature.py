"""
Create the data for megaM model
"""
import os
import re
from collections import defaultdict
from nltk.stem.wordnet import WordNetLemmatizer

from idlelib.IOBinding import encoding

lmtzr = WordNetLemmatizer()

labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
f1 = open("C:/Users/sai vishnu/workspace/NewCorrect/StopWords.txt", "r", errors='ignore')
genres_data_dict = defaultdict(int)      
count = 0
final =""
final1 = ""
stopWords = []

for i in f1.read().split():
    stopWords.append(i)
    

def create_data():
    global genres_data_dict, final, final1
    for label in labels:
        path_name = sys.argv[1]
        genres_data_dict[label]=read_files(path_name, label)
    for k1,v in genres_data_dict.items():
        if k1=="Comedy":
            label = "0"
        elif k1=="Romance":
            label = "1"
        elif k1=="Drama":
            label = "2"
        elif k1=="Horror":
            label = "3"
        elif k1=="Science_Fiction":
            label = "4"
        count = 0
            
        for k2,v in v[0].items():
            count += 1
            final = ""    
            final += label+" "+"CLASSBEGIN "
            for k,v in v.items():
                final += k+" "+str(v)+" " 
            final += ("\n")
            if(count<20):
                f1 = open('final.txt', 'a+', errors='ignore' )
                f1.write(final)
                f1.close()
            if(count<20):
                f_tester = open('tester.txt', 'a+', errors='ignore' )
                f_tester.write(final)
                f_tester.close()
                f_movie = open('test_movie.txt', 'a+', errors='ignore' )
                f_movie.write(k2+"\n")
                f_movie.close()
        
def read_files(path, label):
    final_dicts = []
    genres_data_dict_1 = defaultdict(int)
    
    
    #fo = open(path,"r", encoding="latin1" )
    for root, dirs, files in os.walk(path+label):
        
        for file in files:
            words_count = defaultdict(int)
            if file.endswith(".txt"):
                val = (root + "/" + file)
                fo =open(val, "r", errors='ignore')
                
                for i in fo.read().split():
                    if re.match("^[A-Za-z0-9_-]*$", i) and i not in stopWords:
                        words_count[lmtzr.lemmatize(i)] += 1
                
                genres_data_dict_1[file] = words_count 

    
   
    final_dicts.append(genres_data_dict_1)
      
    return final_dicts    
       
            
                 
                

create_data()