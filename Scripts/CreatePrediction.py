import os
import sys




user = "banana"

test_file = sys.argv[1]
prediction = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/prediction.csv"
#
#./fasttext predict /Users/sebastian/Desktop/Fasttext_kaggle/hate_model_v1.bin
# /Users/sebastian/Desktop/Fasttext_kaggle/test_hate.txt >
# /Users/sebastian/Desktop/Fasttext_kaggle/predection_h1.csv
#

# ModelFile can be deleted everytime
modelFile = "/Users/"+user+"/Desktop/Fasttext_kaggle/toxic_model_v3.bin"
fastText = "./Users/banana/Desktop/fastText-0.1.0/fastText"



os.system("python3 "+str(fastText)+" predict "+modelFile+" "+test_file+" > "+prediction)
