import os
import sys
import json

genre_dict = {}
genre_count = {}
total_genre_count = 0
total_list = []
comedy_dict = {}
romance_dict = {}
model = {}
label_files = {}
total_file_count = 0
#labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
labels = ["Com", "Rom", "Dra", "Hor", "Sci"]

def create_prob():
    global total_file_count
#     path_Comedy = "C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/Comedy"
#     path_Drama = "C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/Drama"
#     path_Romance = "C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/Romance"
#     path_Horror = "C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/Horror"
#     path_Science_Fiction = "C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/Science_Fiction"
    #for comedy :
    for label in labels:
        path_name = str("C:/Users/sai vishnu/workspace/Movie_Genre_Prediction/Data/Train/") + str(label)
        read_files(path_name, label)
    print(str(genre_dict.keys()))
    combined_vocab_count = len(set(total_list))
    print(str(combined_vocab_count))
    print(str(genre_count))
    add_one_smoothing()
    for label in labels:
        for k,v in genre_dict[label].items():
            calculate_probability(k, label, combined_vocab_count, genre_count[label])
    print(model.keys()) 
    for label in labels:
        total_file_count += len(label_files[label]) 
    op = open("nbmodel.txt", 'w')
    for label in labels:
        count = len(label_files[label])
        P_label = float(count/ total_file_count)
        P_not_label = float((total_file_count - count)/ total_file_count)
        op.write("P_"+label+":"+str((P_label))+"\n")
        op.write("P_not_"+label+":"+str((P_not_label))+"\n")
    json_data = json.dumps(model)
    op.write(json_data)
    op.close()

# spam_count = sum(list(spam_dict.values()))
# ham_count = sum(list(ham_dict.values()))    
    
    
def read_files(path1, label):
    global genre_dict, total_list, genre_count, total_genre_count
    #label_files = []
    label_dict = {}
    label_files[label] = []
    path = path1
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".txt"):
                if label in os.path.join(root, file):
                    label_files[label].append(os.path.join(root, file))
                #elif "ham" in os.path.join(root, file):
                    #notlabel_files.append(os.path.join(root, file))

    for file in label_files[label]:
        fp = open(file, "r", encoding="latin1")
        contents = fp.read()
        tokens = contents.split()
        for token in tokens:
            label_dict[token] = label_dict.get(token, 0) + 1
            total_list.append(token)
        fp.close()
        genre_dict[label] = label_dict
        genre_count[label]= sum(list(genre_dict[label].values()))
        total_genre_count += genre_count[label]
#        total_list.append(list(genre_dict[label].keys()))
        #genre_dict_list.append(label_dict)

#     for file in ham_files:
#         fp = open(file, "r", encoding="latin1")
#         contents = fp.read()
#         tokens = contents.split()
#         for token in tokens:
#             ham_dict[token] = ham_dict.get(token, 0) + 1
#         fp.close()
    

def add_one_smoothing():
    global spam_dict, ham_dict
    combined_vocab_list = list(set(total_list))
    for word in combined_vocab_list:
        for label in labels:
            if word not in genre_dict[label]:
                genre_dict[label].update({word: 0})


def output(word, label, value):
    global model
    key = str(word+"_"+label)
    model.update({key: value})


def calculate_probability(word, label, combined_vocab_count, count):
    num = 0
    for label1 in labels:
        if label1 != label:
            num += int(genre_dict[label1][word]+1)
    den = total_genre_count - count + combined_vocab_count
    value = float(num / den)
    output(word, "not_"+label, value)
    num = int(genre_dict[label][word]+1)
    den = count + combined_vocab_count
    value = float(num / den)
    output(word, label, value)


# read_files()
# add_one_smoothing()
# 
# combined_vocab_count = len(set(list(spam_dict.keys()) + list(ham_dict.keys())))
# spam_count = sum(list(spam_dict.values()))
# ham_count = sum(list(ham_dict.values()))
# 
# op = open("nbmodel.txt", 'w')
# for each in spam_dict:
#     calculate_probability(each, "spam", combined_vocab_count, spam_count)
# for each in ham_dict:
#     calculate_probability(each, "ham", combined_vocab_count, ham_count)
# 
# spam_files_count = len(spam_files)
# ham_files_count = len(ham_files)
# print(spam_files_count, ham_files_count)
# total_files = spam_files_count+ham_files_count
# P_spam = float(spam_files_count/total_files)
# P_ham = float(ham_files_count/total_files)
# op.write("P_spam"+":"+str((P_spam))+"\n")
# op.write("P_ham"+":"+str((P_ham))+"\n")
# 
# json_data = json.dumps(model)
# op.write(json_data)
# op.close()
create_prob()