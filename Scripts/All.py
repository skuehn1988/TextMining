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

path = "/Users/sebastian/Desktop/Fasttext_kaggle/"
input_file = "/Users/sebastian/Desktop/Fasttext_kaggle/clean.csv"
output_file = "/Users/sebastian/Desktop/Fasttext_kaggle/toxic_output.csv"
output_file_hate = "/Users/sebastian/Desktop/Fasttext_kaggle/hate_output.csv"


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
    if deleted is "hate":
        writer.writerow(["__label__" + deleted + " " + content])
        writer_txt.write("__label__" + deleted + " " + content + "\n")
    else:
        writer.writerow(["__label__" + deleted + " " + content])
        writer_txt.write("__label__" + deleted + " " + content + "\n")


with open(input_file, "r", encoding="utf-8") as csvfile:
    row_count = (sum(1 for line in open(input_file)))
    print(row_count)
    output_file = open(output_file, "w", encoding="utf-8")
    writer_txt = open(path+"output.txt", "w")
    writer = csv.writer(output_file)
    reader = csv.DictReader(csvfile)
    data = [row for row in reader]
    #writer.writerow(["id", "content", "deleted"])
    ids = 0
    # set number of ratio here or set a very high number no ratio
   # truth = 200000
    #false = 200000

     # place column name here (toxic , identity_hate)
    name_of_row = "identity_hate"
    name_of_row_ = "toxic"

    for row in data:
        #if(row[name_of_row] == "0" and false >= 0 or row[name_of_row_] == "0" and false >= 0):
           # false = false-1
            id = row["id"]
            content = row["comment_text"]
            content = blacklist(content)
            deleted = row[name_of_row]
            deleted_= row[name_of_row_]
            if(deleted == "0.0"):
                deleted = str(deleted)
                deleted = "nohate"

            if(deleted_ == "0.0"):
                deleted_ = str(deleted_)
                deleted_ = "notoxic"

            if(deleted == "1.0"):
                deleted = str(deleted)
                deleted = "hate"

            if(deleted_ == "1.0"):
                deleted_ = str(deleted_)
                deleted_ = "toxic"

            #print([id, content, deleted])
            writeToFile(writer, id, content, deleted, deleted_)
            ids = ids +1

        # if(row[name_of_row] == "1" and truth >= 0 or row[name_of_row_] == "1" and truth >= 0):
        #     truth = truth-1
        #     id = row["id"]
        #     content = row["comment_text"]
        #     content = blacklist(content)
        #     deleted = row[name_of_row]
        #     deleted_= row[name_of_row_]
        #
        #     #print([id, content, deleted])
        #     writeToFile(writer, id, content, deleted, deleted_)
        #     ids = ids +1
        #
        # if(truth == 0 and false == 0):
        #     output_file.close()
        #     exit()

        #else:
            print(str((ids/row_count)*100)[:5] + " %")
