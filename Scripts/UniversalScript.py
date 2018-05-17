# -*- coding: utf-8 -*-


import csv

# TOdo Must have
# Done To Lower
# done count Rows -  make percentage 159.571
# toxic number of 0 : 144.277 number of 1 : 15.294 =  90,4/9,6
# hate number of 0 : 158166 number of 1 : 1405
# Done find quotes / delete
# Todo kill Time

# Todo Nice to HAve
# Todo REST API übersetzung
# ToDo HelpOut Embedding
# Todo https://en.wikipedia.org/wiki/Bootstrap_aggregating


input_file = "/Users/banana/Desktop/TextMining/test_hate__.csv"
output_file = "/Users/banana/Desktop/TextMining/nothingbutthetruth.csv"

def blacklist(string):
    string = str(string)
    string = string.lower()
    blacklistedWords = ['\\n', '\\r', '@', '"', "(talk)", "/talk/"]
    for x in range(len(blacklistedWords)):
        string = str(string).replace(blacklistedWords[x],"")
        string = str(string).replace("  ", " ")
    return string


def writeToFile(writer, id, content, deleted):
    # id = 1,2,3
    # content = comments
    # deleted = 0 or 1
    writer.writerow([deleted[9:11]])

# def deleteSpaces(string):
#     string = str(string)
#     string.replace("  ", " ")
#     return

# __label__ [9:11]

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
        print([id, content, deleted])
        writeToFile(writer, id, content, deleted)

    output_file.close()
    exit()
