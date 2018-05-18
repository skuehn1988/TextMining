# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
#
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division, absolute_import, print_function




import os
from fastText import train_supervised


user = "banana"

def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


if __name__ == "__main__":
    train_data = os.path.join(os.getenv("/Users/"+user+"/Desktop/Fasttext_kaggle/", ''), "/Users/"+user+"/Desktop/Fasttext_kaggle/train_toxic.txt")
    #valid_data = os.path.join(os.getenv("/Users/"+user+"/Desktop/Fasttext_kaggle/", ''), "/Users/"+user+"/Desktop/Fasttext_kaggle/test_toxic.txt")

    # Run 1     model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=1, maxn=1, lr=0.8, dim=100, epoch=75 , bucket=2000000,loss='softmax')

    # Run 2     model = train_supervised(input=train_data, minCount=1, wordNgrams=3, minn=2, maxn=2, lr=1, dim=100, epoch=100 , bucket=2000000,loss='softmax')

    # Run 3     model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=2, maxn=2, lr=1, dim=100, epoch=200 , bucket=2000000,loss='softmax')

    # Run 4     model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=2, maxn=2, lr=0.8, dim=100, epoch=150 , bucket=3000000,loss='softmax')

    # Run 5     model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=1, maxn=1, lr=0.8, dim=100, epoch=75 , bucket=2000000, loss='hs')

    # Run 6     model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=1, maxn=1, lr=0.8, dim=100, epoch=75 , bucket=2000000, loss='ns')


    # train_supervised uses the same arguments and defaults as the fastText cli
    model = train_supervised(input=train_data, minCount=1, wordNgrams=2, minn=1, maxn=1, lr=0.8, dim=100, epoch=75 , bucket=2000000, loss='ns')
    #model = train_supervised(input=train_data, epoch=1)
    model.save_model("/Users/"+user+"/Desktop/Fasttext_kaggle/toxic_model_v3.bin")
    #model.save_model("/Users/"+user+"/Desktop/Fasttext_kaggle/cooking.ftz")

print("fertig")
# now run this
# Dominiks-MacBook-Pro:fastText-0.1.0 banana$ ./fasttext predict /Users/banana/Desktop/Fasttext_kaggle/toxic_model_v3.bin /Users/banana/Desktop/Fasttext_kaggle/test_toxic.txt > /Users/banana/Desktop/Fasttext_kaggle/predection_d6.csv
# Dominiks-MacBook-Pro:fastText-0.1.0 banana$

# after that run the script to make a table that either fucks everything up or just add you a head with deleted and than 0 , 1 ;

