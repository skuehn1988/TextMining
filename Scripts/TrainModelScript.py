# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
from __future__ import absolute_import
from __future__ import division
from __future__ import division, absolute_import, print_function
from __future__ import print_function
from __future__ import unicode_literals

import os
import sys

from fastText import train_supervised

new_output_file = "/Users/banana/PycharmProjects/TextMiningCleaning/TextMining/Scripts/Models/train.txt"

try:
    # minCount = sys.argv[1]
    # wordNgrams = sys.argv[2]
    # minn = sys.argv[3]
    # maxn = sys.argv[4]
    # lr = sys.argv[5]
    # dim = sys.argv[6]
    # epoch = sys.argv[7]
    # bucket = sys.argv[8]
    # loss = sys.argv[9]

    minCount = int(sys.argv[1])
    wordNgrams = int(sys.argv[2])
    minn = int(sys.argv[3])
    maxn = int(sys.argv[4])
    lr = float(sys.argv[5])
    dim = int(sys.argv[6])
    epoch = int(sys.argv[7])
    bucket = int(sys.argv[8])
    loss = sys.argv[9]

except:
    print("for bash: python TrainModelScript.py  minCount wordNgrams minn maxn lr dim epoch bucket loss")
    print(" example : python3 TrainModelScript.py 1 2 1 1 0.8 100 75 2000000 ns")
    print("No input_file and output_file provided.")
    print("Place a file with csv ending")
    print("For example: ")


user = "banana"

def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))



if __name__ == "__main__":
    train_data = os.path.join(os.getenv("/Users/"+user+"/Desktop/Fasttext_kaggle/", ''), new_output_file)
    #valid_data = os.path.join(os.getenv("/Users/"+user+"/Desktop/Fasttext_kaggle/", ''), "/Users/"+user+"/Desktop/Fasttext_kaggle/test_toxic.txt")


    # train_supervised uses the same arguments and defaults as the fastText cli

    model = train_supervised(input=train_data, minCount=minCount, wordNgrams=wordNgrams, minn=minn, maxn=maxn, lr=lr, dim=dim, epoch=epoch, bucket=bucket, loss=loss)

    #model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=1, maxn=1, lr=0.8, dim=100, epoch=75 , bucket=2000000, loss='ns')





    model.save_model("/Users/"+user+"/Desktop/Fasttext_kaggle/toxic_model_v3.bin")

    file = open(new_output_file, "r")


    #
    # for line in file:
    #
    #     line_blubb = line.rstrip()
    #     pred = model.predict(line_blubb)
    # print(pred)
    #
    # file.close()



print("fertig")


# now run this


# Dominiks-MacBook-Pro:fastText-0.1.0 banana$ ./fasttext predict /Users/banana/Desktop/Fasttext_kaggle/toxic_model_v3.bin /Users/banana/Desktop/Fasttext_kaggle/test_toxic.txt > /Users/banana/Desktop/Fasttext_kaggle/predection_d6.csv
# Dominiks-MacBook-Pro:fastText-0.1.0 banana$

# after that run the script to make a table that either fucks everything up or just add you a head with deleted and than 0 , 1 ;

