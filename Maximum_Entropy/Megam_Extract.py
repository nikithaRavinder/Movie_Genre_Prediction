"""
Create the data for megaM model
"""
import os
from collections import defaultdict
from idlelib.IOBinding import encoding
import re
import sys
labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
genres_data_dict = defaultdict(int)      

final =""
final1 = ""
def create_data():
    global genres_data_dict, final, final1
    for label in labels:
        path_name = sys.argv[1]; # Path for the training folder
        genres_data_dict[label]=read_files(path_name, label)
    for k1,v in genres_data_dict.items():
        if True:
            j=v
            count_genre = 0
            count_not_genre = 0
            for k,v in v[0].items():
                count_genre += 1
                final = ""
                
                final += "0"+" "
                for k,v in v.items():
                    final += k+" "+str(v)+" " 
                final += ("\n")
                if(count_genre< 1000):
                    f1 = open('output_megam_'+k1+'.txt', 'a+', errors='ignore' )
                    f1.write(final)
                    f1.close()
            for k,v in j[1].items():
                count_not_genre += 1
                final1 = ""
                final1 += "1"+" "
                for k,v in v.items():
                    final1 += k+" "+str(v)+" "
                final1 += "\n"
                if(count_not_genre<1500):
                    f2 = open('output_megam_'+k1+'.txt', 'a+', errors='ignore')
                    f2.write(final1) 
                    f2.close()
          
        
         
        
    
            
                
    
        
def read_files(path, label):
    final_dicts = []
    genres_data_dict_1 = defaultdict(int)
    genres_data_dict_2 = defaultdict(int) 
    
    #fo = open(path,"r", encoding="latin1" )
    for root, dirs, files in os.walk(path+label):
        
        for file in files:
            words_count = defaultdict(int)
            if file.endswith(".txt"):
                val = (root + "/" + file)
                fo =open(val, "r", errors='ignore')
                
                for i in fo.read().split():
                    if re.match("^[A-Za-z0-9_-]*$", i):
                        words_count[i] += 1
                
                genres_data_dict_1[file] = words_count 

    
    for x in labels:
        if label not in x:
            for root, dirs, files in os.walk(path+x):
                for file in files:
                    words_count1 = defaultdict(int)
                    if file.endswith(".txt"):
                        val = (root + "/" + file)
                        fo =open(val, "r",  errors='ignore')
                        
                        for i in fo.read().split():
                            if re.match("^[A-Za-z0-9_-]*$", i):
                                words_count1[i] += 1
                        genres_data_dict_2[file] = words_count1
    
    final_dicts.append(genres_data_dict_1)
    final_dicts.append(genres_data_dict_2)   
    return final_dicts    
       
            
                 
                

create_data()