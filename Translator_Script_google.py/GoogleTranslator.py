# -*- coding: utf-8 -*-


import csv

input_file = "/Users/banana/Desktop/input_translation.csv"
output_file = "/Users/banana/Desktop/output_google_translation.csv"



def writeToFile(writer, id, content, deleted):
    writer.writerow([id, content, deleted])

def translate_(stringrow, input_language, output_language):
    from_language = input_language
    to_language = output_language
    translation = pydeepl.translate(stringrow, to_language, from_lang=from_language)
    return translation




def read_input_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as csv_file:
        output_file = open(output_file, "w", encoding="utf-8")
        writer = csv.writer(output_file)
        reader = csv.reader(csv_file)
        data = [row for row in reader]
        id = 0
        writer.writerow(["id", "content", "deleted"])
        for row in data:
            try:
                content = row[1]
                deleted = row[2]
                # translation call here
                #content = translate_(translate_(content, "DE", "EN"), "EN", "DE")
                writeToFile(writer, id, content, deleted)
                id = id+1
                print((str((id/296900)*100)+" %")[:5] + " at id: "+ str(id))
            except:
                # if we get errors i will add logger here but only if we get errors.

                print("Error while Tranlating id :" + str(id) )
        output_file.close()
        exit()

read_input_file(input_file, output_file)
