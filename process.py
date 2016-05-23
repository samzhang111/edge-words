# coding: utf-8
import bs4
import pandas as pd
import nltk
from preprocess import preprocess
from collections import defaultdict
from operator import itemgetter

retirement_html = open('retirement.html').read()
retirement_soup = bs4.BeautifulSoup(retirement_html)
responses = retirement_soup.select('.view-content .response .views-field-body')
text_responses = [response.text for response in responses]

title_responses = [x.text for x in retirement_soup.select('.view-content .response .response-title')]
responses_dict = dict(title=title_responses, content=text_responses)

df = pd.DataFrame(responses_dict)
df_responses = df[1:]
df_responses.to_csv('responses.csv', index=False, columns=['title', 'content'])

unique_words_per_article = []
for response in text_responses[1:]:
    unique_words_per_article.append(set(preprocess(response)))

intersections = defaultdict(int)
for article in unique_words_per_article:
    for word in article:
        intersections[word] += 1

sorted(intersections.items(), key=itemgetter(1))
vocab_in_order = sorted(intersections.items(), key=itemgetter(1))

print(vocab_in_order[-100:])
