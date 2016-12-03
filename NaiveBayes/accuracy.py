__author__ = "Nikitha Ravinder"

belongs, classified, correctly_classified = {}, {}, {}
labels = ["Romance", "Comedy", "Drama", "Horror", "Science_Fiction"]
file = open("output.txt", "r").readlines()
for line in file:
    op_label = line.split("\t")[1]
    path = line.split("\t")[0]
    fname = path[path.rfind("/")+1:]
    for label in labels:
        if label not in belongs:
            belongs[label] = 0
        if label not in classified:
            classified[label] = 0
        if label not in correctly_classified:
            correctly_classified[label] = 0

        if label in fname:
            belongs[label] += 1
        if label in op_label:
            classified[label] += 1
            if label in fname:
                correctly_classified[label] += 1

#print(belongs)
#print(classified)
#print(correctly_classified)

for label in labels:
    label_precision = float(correctly_classified[label]) / float(classified[label])
    label_recall = float(correctly_classified[label]) / float(belongs[label])
    label_fscore = (2 * label_precision * label_recall) / (label_precision + label_recall)

    print(label + " : Precision= {0}, Recall= {1}, F-Score= {2}".format(label_precision, label_recall, label_fscore))




