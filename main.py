import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

nltk.download('punkt')

url = 'https://www.noen.at/in-ausland/oesterreich-grenzkontrollen-bis-10-jaenner-verstaerkt-arbeitsmarkt-bundesheer-epidemie-reisen-zusammenfassung-oesterreich-238488125'
article = Article(url)

article.download()
article.parse()

article.nlp()

print(f'Title: {article.title}')
print(f'Authors: {article.authors}')
print(f'Publication Date: {article.publish_date}')
print(f'Summary: {article.summary}')