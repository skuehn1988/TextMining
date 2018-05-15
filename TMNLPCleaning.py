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
# Done REST API übersetzung
# ToDo HelpOut Embedding
# Todo https://en.wikipedia.org/wiki/Bootstrap_aggregating

path = "/Users/banana/Desktop/TextMining/"
input_file = "/Users/banana/Desktop/TextMining/train_preprocessed.csv"
output_file = "/Users/banana/Desktop/TextMining/train_preprocessed_clean_identity.csv"

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


def writeToFile(writer, id, content, deleted, deleted_):
    writer.writerow(["__label__" + deleted + " " + "__label__" + deleted_ + " " + content])
    writer_txt.write("__label__" + deleted + " " + "__label__" + deleted_ + " " + content + "\n")



with open(input_file, "r", encoding="utf-8") as csvfile:
    row_count = (sum(1 for line in open(input_file)))
    print(row_count)
    output_file = open(output_file, "w", encoding="utf-8")
    writer_txt = open(path+"output.txt", "w")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    ids = 0

    name_of_row = "identity_hate"
    name_of_row_ = "toxic"
    for row in data:

            id = row["id"]
            content = row["comment_text"]
            content = blacklist(content)
            deleted = row[name_of_row]
            deleted_= row[name_of_row_]
            if(deleted == "0.0"):
                deleted = str(deleted)
                deleted = "0"

            if(deleted_ == "0.0"):
                deleted_ = str(deleted_)
                deleted_ = "0"

            if(deleted == "1.0"):
                deleted = str(deleted)
                deleted = "1"

            if(deleted_ == "1.0"):
                deleted_ = str(deleted_)
                deleted_ = "1"

            #print([id, content, deleted])
            writeToFile(writer, id, content, deleted, deleted_)
            ids = ids +1


            print(str((ids/row_count)*100)[:5] + " %")

