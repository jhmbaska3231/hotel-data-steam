# https://www.kaggle.com/datasets/borhanitrash/twitter-financial-news-sentiment-dataset

# pip3 install kagglehub
import kagglehub

path = kagglehub.dataset_download("borhanitrash/twitter-financial-news-sentiment-dataset")

print("Path to dataset files:", path)