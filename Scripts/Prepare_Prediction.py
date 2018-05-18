# -*- coding: utf-8 -*-
# header muss geschrieben werden um "deleted" in den header zu schreiben

import pandas as pd
from sklearn import metrics
from sklearn.metrics import classification_report
import csv
from sklearn.metrics import confusion_matrix

user = "banana"

input_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/predection_v2.csv"
output_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/truth_prediction_v2.csv"

def prepare_prediction(file):
    with open('file.csv',newline='') as f:
        r = csv.reader(f)
        data = [line for line in r]
    with open('file.csv','w',newline='') as f:
        w = csv.writer(f)
        w.writerow(['deleted'])
        w.writerows(data)
    return f


def writeToFile(writer, id, content, deleted):
    # id = 1,2,3
    # content = comments
    # deleted = 0 or 1
    writer.writerow([deleted[9:11]])


with open(input_file, "r", encoding="utf-8") as csvfile:
    output_file = open(output_file, "w", encoding="utf-8")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    # header here
    writer.writerow(["deleted"])
    # place column name here (toxic , identity_hate)
    name_of_row = "deleted"
    for row in data:
        row[name_of_row][9:11]#and false >= 0 or row["toxic"] != "False" and false >= 0):
        content = row["deleted"]
        deleted = row[name_of_row]
        writeToFile(writer, id, content, deleted)
    output_file.close()
    exit()
    
categories = ["deleted"]


def to_binary(predictions):
    for category in categories:
        predictions[category] = [1 if row > 0.5 else 0 for row in predictions[category]]
    return predictions


def get_f1_results(truth, predictions, name):
# Label in Confusion Matrix Toxic und Not Toxic
    target_names = ['not toxic','toxic']
    predictions = to_binary(predictions)

    print(name + ": " + str(metrics.classification_report(truth[categories], predictions[categories], target_names=target_names)))
    print("Micro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='micro')))
    print("Macro: " + str(metrics.f1_score(truth[categories], predictions[categories], average='macro')))
    print("Average: " + str(metrics.f1_score(truth[categories], predictions[categories], average='weighted')))

    ## print(classification_report(y_true, y_pred, target_names=target_names))
     ##        precision    recall  f1-score   support

if _name_ == "_main_":
    truth = pd.read_csv("/Users/"+user+"/Desktop/Fasttext_kaggle/truth.csv")

    prediction1 = pd.read_csv("/Users/"+user+"/Desktop/Fasttext_kaggle/truth_prediction_v2.csv")

    get_f1_results(truth, prediction1, "Prediction 1")
    
confusion_matrix(truth, prediction1)
