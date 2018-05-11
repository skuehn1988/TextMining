# -*- coding: utf-8 -*-


import csv

# TOdo Must have
# Done To Lower
# done count Rows -  make percentage 159.571
# toxic :
# Done find quotes / delete
# Todo kill Time

# Todo Nice to HAve
# Todo REST API übersetzung
# ToDo HelpOut Embedding
# Todo https://en.wikipedia.org/wiki/Bootstrap_aggregating


input_file = "/Users/banana/Desktop/TextMining/train.csv"
output_file = "/Users/banana/Desktop/TextMining/train_clean_identity.csv"
toxic_counter = 0
nontoxic_counter = 0


def blacklist(string):
    string = str(string)
    string = string.lower()
    blacklistedWords = ['\\n', '\\r', '@', '"', "(talk)", "/talk/"]
    for x in range(len(blacklistedWords)):
        string = str(string).replace(blacklistedWords[x],"")
    return string


def writeToFile(writer, id, content, deleted):
    writer.writerow([id, content, deleted])


with open(input_file, "r", encoding="utf-8") as csvfile:
    output_file = open(output_file, "w", encoding="utf-8")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    ids = 0
    truth = 100000
    false = 100000
    for row in data:
        if(row["toxic"] == "0" and false >= 0 or row["toxic"] == "False" and false >= 0):
            false = false-1
            #id_ = row["id"]
            id = row["id"]
            content = row["comment_text"]
            deleted = row["identity_hate"]
            print([id, content, deleted])
            writeToFile(writer, id, content, deleted)
            ids = ids +1


        if(row["toxic"] == "1" and truth >= 0 or row["toxic"] == "True" and truth >= 0):
            truth = truth-1
            #id_ = row["id"]
            id = row["id"]
            content = row["comment_text"]
            deleted = row["identity_hate"]
            print([id, content, deleted])
            writeToFile(writer, id, content, deleted)
            ids = ids +1
        if(truth == 0 and false == 0):
            output_file.close()
            exit()
        else:
            print("truth : ", truth)
            print("false : ", false)
