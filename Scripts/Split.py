import os
from fastText import train_supervised

os.system('head -n 80000 /Users/sebastian/Desktop/Fasttext_kaggle/output.txt > /Users/sebastian/Desktop/Fasttext_kaggle/train.txt')
os.system('tail -n 30000 /Users/sebastian/Desktop/Fasttext_kaggle/output.txt > /Users/sebastian/Desktop/Fasttext_kaggle/test.txt')
