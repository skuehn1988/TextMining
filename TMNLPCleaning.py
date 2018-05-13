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


input_file = "/Users/banana/Desktop/TextMining/train.csv"
output_file = "/Users/banana/Desktop/TextMining/train_clean_identity.csv"

def blacklist(string):
    string = str(string)
    string = string.lower()
    blacklistedWords = ['\\n', '\\r', '@', '"', "(talk)", "/talk/", "|", "{", "}"]
    for x in range(len(blacklistedWords)):
        string = str(string).replace(blacklistedWords[x],"")
        string = str(string).replace("  ", " ")
        string = str(string).replace("::", ":")
        string = str(string).replace("==", "=")
        string = str(string).replace("--", "-")
        string = str(string).replace("__", "_")

    return string


def writeToFile(writer, id, content, deleted):
    writer.writerow([id, content, deleted])


with open(input_file, "r", encoding="utf-8") as csvfile:
    row_count = (sum(1 for line in open(input_file))*0.2839)
    print(row_count)
    output_file = open(output_file, "w", encoding="utf-8")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    writer.writerow(["id", "content", "deleted"])
    ids = 0
    # set number of ratio here or set a very high number no ratio
    truth = 200000
    false = 200000
     # place column name here (toxic , identity_hate)
    name_of_row = "identity_hate"
    for row in data:
        if(row[name_of_row] == "0" and false >= 0 or row["toxic"] == "False" and false >= 0):
            false = false-1
            id = row["id"]
            content = row["comment_text"]
            content = blacklist(content)
            deleted = row[name_of_row]
            #print([id, content, deleted])
            writeToFile(writer, id, content, deleted)
            ids = ids +1

        if(row[name_of_row] == "1" and truth >= 0 or row["toxic"] == "True" and truth >= 0):
            truth = truth-1
            id = row["id"]
            content = row["comment_text"]
            content = blacklist(content)
            deleted = row[name_of_row]
            #print([id, content, deleted])
            writeToFile(writer, id, content, deleted)
            ids = ids +1

        if(truth == 0 and false == 0):
            output_file.close()
            exit()

        else:
            print(str((ids/row_count)*100)[:5] + " %")

