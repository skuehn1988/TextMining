import os
import sys
import fastText
from sklearn.linear_model import LogisticRegression


user = "banana"

test_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Models/test.txt"
prediction = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/prediction.csv"
#
#./fasttext predict /Users/sebastian/Desktop/Fasttext_kaggle/hate_model_v1.bin
# /Users/sebastian/Desktop/Fasttext_kaggle/test_hate.txt >
# /Users/sebastian/Desktop/Fasttext_kaggle/predection_h1.csv
#

modelFile = "/Users/"+user+"/Desktop/Fasttext_kaggle/toxic_model_v3.bin"
fastText = "./Desktop/fastText-0.1.0/fasttext"

file = open(test_file, "r")
model = open(modelFile)



# ModelFile can be deleted everytime
try:
    x = str(fastText)+" predict "+modelFile+" "+test_file+" > "+prediction
    os.system(x)
    print(x)
except:
    print("done")
