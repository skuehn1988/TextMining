import os
import fasttext

user = "banana"
try:
    os.system('head -n 80000 /Users/'+user+'/Desktop/Fasttext_kaggle/output_hate.txt > /Users/'+user+'/Desktop/Fasttext_kaggle/train.txt')
    os.system('tail -n 30000 /Users/'+user+'/Desktop/Fasttext_kaggle/output_toxic.txt > /Users/'+user+'/Desktop/Fasttext_kaggle/test.txt')
except:
    print("sorry this didn't work for at least one file")
