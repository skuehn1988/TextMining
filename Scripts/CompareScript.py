# -*- coding: utf-8 -*-
# header muss geschrieben werden um "deleted" in den header zu schreiben

import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report
import csv
from sklearn.metrics import confusion_matrix

user = "sebastian"

input_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/predection_v2.csv"
output_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/truth_prediction_v3.csv"
truth_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/truth.csv"



data = pd.read_csv(input_file, header=None)
data.columns = ["deleted"]
#data.drop(data.index[0], inplace=True)
data.to_csv("/Users/"+user+"/Desktop/Fasttext_kaggle/predection_v2.csv", index=False)



def writeToFile(writer, id, content):
    # id = 1,2,3
    # content = comments
    # deleted = 0 or 1
    writer.writerow([content[9:11]])


with open(input_file, "r", encoding="utf-8") as csvfile:
    output_file = open(output_file, "w", encoding="utf-8")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]

    writer.writerow(["deleted"])
    # place column name here (toxic , identity_hate)
    name_of_row = "deleted"
    for row in data:
        row[name_of_row]#and false >= 0 or row["toxic"] != "False" and false >= 0):
        content = row["deleted"]
        writeToFile(writer, id, content)
output_file.close()
input_file.close()
##F1 Score
