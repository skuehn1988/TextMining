import sys

UniversalScript = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/UniversalScript.py"
CsvToTxt = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/UniversalScript.py"
TrainModelScript =

try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    csvtotxt_file = sys.argv[3]
    minCount = sys.argv[1]
    wordNgrams = sys.argv[2]
    minn = sys.argv[3]
    maxn = sys.argv[4]
    lr = sys.argv[5]
    dim = sys.argv[6]
    epoch = sys.argv[7]
    bucket = sys.argv[8]
    loss = sys.argv[9]
except:
