__author__ = "Megha Sharma"
import sys
import os
import json
import math
with open('per_model.txt','r',encoding="latin1") as f:
    params = json.load(f)
labels = ["Comedy", "Romance", "Drama", "Horror", "Science_Fiction"]
st = ""
res = {}
#dirname = str(sys.argv[1])
#print(dirname)
#dirname = "Test"
dirname = "Data/Test"
count = {}
for dirpath, dirs, files in os.walk(dirname):
    for filename in files:
        if filename[filename.rfind(".") + 1:] == "txt":
            fname = os.path.join(dirpath, filename)
            f = open(fname, "r", encoding="latin1")
            text = f.read()
            f.close()
            tokens = text.split()
            for label in labels:
                if label not in res:
                    res[label] = [[0,0],[0,0]]
                w = params[label]["w"]
                b = params[label]["b"]
                a = b
                for token in tokens:
                    if token in w:
                        a = a + w[token]
                #print(str(fname) +" "+ label + "-"+ str(a))
                if (a > 0):
                    st = st + label +str(fname)+"\n"
                    j = 0
                else:
                    st = st + "not " + label + str(fname) + "\n"
                    j = 1
                if label in fname:
                    i = 0
                else:
                    i = 1
                res[label][i][j] += 1


wname = "per_output.txt"
wfile = open(wname, 'w+',encoding="latin1")
wfile.write(st)
wfile.close()

#print(st)
print(res)
for label in labels:
    sprec = res[label][1][1] / (res[label][1][1] + res[label][0][1])
    srec = res[label][1][1] / (res[label][1][1] + res[label][1][0])
    sfsc = 2 * sprec * srec / (sprec + srec)
    print("\n not "+label+ "1a. precision: "+str(sprec)+"\n1b. recall: "+ str(srec) + "\n1c. F1 score: "+str(sfsc))
    hprec = res[label][0][0] / (res[label][0][0] + res[label][1][0])
    hrec = res[label][0][0] / (res[label][0][0] + res[label][0][1])
    hfsc = 2 * hprec * hrec / (hprec + hrec)
    print("\n" + label + "\nprecision: " + str(hprec) + "\nrecall: " + str(hrec) + "\nscore: " + str(
        hfsc))

