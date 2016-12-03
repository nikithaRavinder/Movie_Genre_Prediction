import sys, os
import glob
from sklearn import svm
import  numpy

c=-1
count = 0;
vocabulary = []
Y= []
n=0
path = "/home/devyanimadan/Downloads/Data/Data/Train"
subdirList =os.listdir(path)
print(subdirList)


for subdir in subdirList:
    print(subdir)
    if subdir.startswith("Sci"):
        #print(subdir)
        c=0
        #print(c)
    if subdir.startswith("Dra"):
            #print(subdir)
            c = 1
            #print(c)
    if subdir.startswith("Hor"):
            #print(subdir)
            c = 2
            #print(c)
    if subdir.startswith("com"):
            #print(subdir)
            c = 3
            #print(c)
    if subdir.startswith("Rom"):
            #print(subdir)
            c = 4
            #print(c)

#for dir, subdirs, files in  os.walk(r"movie_genere"):
    #subdir = os.path.join(dir,subdirs)
    #print(subdirs)
    temp_path= path+'/'+subdir
    #print(temp_path)
    for root,folder,files in os.walk(temp_path):
        #print(files)
        for file in files:
            print(file)
            Y.append(c)
            #print(X)
            new_path = os.path.join(path,subdir)
            #print(new_path)
            file_path = os.path.join(new_path,file)
            #print(file_path)
            fopen=open(file_path,"r")
            n += 1
        #print("inside file for")
            for lines in fopen:
                for word in lines.split():
                    if word not in vocabulary:
                        vocabulary.append(word)

print(vocabulary)
print (len(vocabulary))
print(Y)
print(len(Y))
i=0
X = [[]]*n
print(type(X[i]))
for subdir in subdirList:
    temp_path = path + '/' + subdir
    for root, folder, files in os.walk(temp_path):
        for file in files:
            new_path = os.path.join(path, subdir)
            file_path = os.path.join(new_path, file)
            fopen = open(file_path, "r")
            new = []
            for word in vocabulary:
                if word in fopen:
                    new.append(1)
                else:
                    new.append(0)
            X[i]=new
            #print(str(i))
            i += 1

#print(X)
print(len(X))
print(len(X[0]))
#X1 = numpy.array(X)
#print(X1.shape)

clf = svm.SVC()
clf.fit(X, Y)

test_list = []

fopen=open("/home/devyanimadan/Downloads/genres_test/61071_Lady_for_a_Day_Drama_Comedy.txt","r")
for lines in fopen:
    for word in vocabulary:
        if word in lines.split():
            test_list.append(1)
        else:
            test_list.append(0)

print(clf.predict(test_list))

#dec = clf.decision_function([[1]])
# dec.shape[1] # 4 classes: 4*3/2 = 6

# clf.decision_function_shape = "ovr"
# dec = clf.decision_function([[1]])
# dec.shape[1]


