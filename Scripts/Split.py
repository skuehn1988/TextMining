import os
from fastText import train_supervised

user = "banana"
os.system('head -n 80000 /Users/'+user+'/Desktop/Fasttext_kaggle/output.txt > /Users/sebastian/Desktop/Fasttext_kaggle/train.txt')
os.system('tail -n 30000 /Users/'+user+'/Desktop/Fasttext_kaggle/output.txt > /Users/sebastian/Desktop/Fasttext_kaggle/test.txt')
