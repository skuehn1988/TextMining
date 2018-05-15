# -*- coding: utf-8 -*-


import csv

user = "banana"


path = "/Users/"+user+"/Desktop/Fasttext_kaggle/"
input_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/clean.csv"
output_file = "/Users/"+user+"/Desktop/Fasttext_kaggle/toxic_output.csv"
output_file_hate = "/Users/"+user+"/Desktop/Fasttext_kaggle/hate_output.csv"


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

            writeToFile(writer, id, content, deleted, deleted_)
            ids = ids +1

            print(str((ids/row_count)*100)[:5] + " %")
