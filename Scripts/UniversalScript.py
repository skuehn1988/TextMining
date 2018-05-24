# -*- coding: utf-8 -*-


import csv
import sys




try:
    input_file = sys.argv[1]
    output_file = sys.argv[2]
except:
    print("for bash: python UniversalScript.py /Users/username/Desktop/Textming/input.csv /Users/username/Desktop/Textming/ouput.csv ")
    print("No input_file and output_file provided.")
    print("Place a file with csv ending")
    print("For example: ")
    print("input.csv and output.csv")
    input_file = input()
    input_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Input/"+str(input_file)
    print("now output.csv file name")
    output_file = input()
    output_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/"+str(output_file)


def writeToFile(writer, id, content, deleted):

    writer.writerow([deleted[9:10]])

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
        #print([id, content, deleted])
        writeToFile(writer, id, content, deleted)
    #print("Universal Script : task done")
    #print("/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Input/")
    #print("/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/")
    output_file.close()
    exit()



