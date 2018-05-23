import sys
import os


UniversalScript = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/UniversalScript.py"
CsvToTxt = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/CsvToTxt.py"
TrainModelScript = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/TrainModelScript.py"
CreatePrediciton = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/CreatePrediction.py"
F1ScoreCalculator = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/F1ScoreCalculator.py"
train_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Input/2500.train.txt"
test_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Input/2500.test.txt"

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    csvtotxt_file = sys.argv[3]
    minCount = sys.argv[4]
    wordNgrams = sys.argv[5]
    minn = sys.argv[6]
    maxn = sys.argv[7]
    lr = sys.argv[8]
    dim = sys.argv[9]
    epoch = sys.argv[10]
    bucket = sys.argv[11]
    loss = sys.argv[12]
    #train = sys.argv[13]
    #test = sys.argv[14]

except:
    print("something wrong")

os.system("python3 "+str(UniversalScript)+" "+"/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Input/"+str(input_file)+" "+"/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/"+str(output_file))
os.system("python3 "+str(CsvToTxt)+" "+"/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/"+str(output_file)+" "+"/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Models/"+str(csvtotxt_file))
os.system("python3 "+str(TrainModelScript)+" "+minCount+" "+wordNgrams+" "+minn+" "+maxn+" "+lr+" "+dim+" "+epoch+" "+bucket+" "+loss)
os.system("python3 "+str(CreatePrediciton)+" "+test_file)



#os.system("python3 "+str(F1ScoreCalculator)+" "+"/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/"+x+" "+y)

#print("minCount:    ",  sys.argv[4])
print("wordNgrams:  ",  sys.argv[5])
print("minn:        ",  sys.argv[6])
print("maxn:        ",  sys.argv[7])
print("lr:          ",  sys.argv[8])
print("dim:         ",  sys.argv[9])
print("epoch:       ", sys.argv[10])
#print("bucket:      ", sys.argv[11])
print("loss:        ", sys.argv[12])
