import csv
import shutil
import sys
import os

template_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/template.txt"
old_output_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Output/output.csv"
new_output_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Models/test.txt"

shutil.copyfile(template_file, new_output_file)




with open(new_output_file, "w") as my_output_file:
    with open(old_output_file, "r") as my_input_file:
        [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
    my_output_file.close()
