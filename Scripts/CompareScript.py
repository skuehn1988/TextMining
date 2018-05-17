# open r
# open r
# open w

import csv
path = "/Users/banana/Desktop/TextMining/Testing/"
kaggle_file =  path+"kaggle-data.csv"
internet_file = path+"train_preprocessed.csv"
output_file = path+"compare_file.csv"



kfile = open(kaggle_file, "r", encoding="utf-8")
ifile = open(internet_file, "r", encoding="utf-8")
output_file = open(output_file, "w", encoding="utf-8")


# for
# write id comment label
# if ifile or kfile is empty than write zero

def writeToFile(writer, id_, content, label1, label2):
    # id = 1,2,3
    # content = comments
    # deleted = 0 or 1
    writer.writerow([id_, content, label1, label2])

def magic(file1, file2, file3):
    writer = csv.writer(output_file)
    variation = [file1, file2]


    output_file.close()
    exit()



magic(ifile, kfile, output_file)
