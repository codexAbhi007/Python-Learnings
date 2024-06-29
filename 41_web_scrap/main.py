from bs4 import BeautifulSoup
import requests

with open(r'Docs\index.html') as html_file:
    soup = BeautifulSoup(html_file,'lxml')

# print(soup.prettify())

# title = soup.title
# print(title)
# print(title.text)
# print(title.tag)


##This returns only the first occurence
article = soup.find('div',class_='article')
# print(article.prettify())

headline = article.h2.a.text
print(headline)

summary = article.p.text
print(summary)


##This returns a list of occurences
articles = soup.find_all('div',class_='article')
# print(articles)

def head_and_summary(articles):
    for article in articles:
        headline = article.h2.a.text
        print(headline)

        summary = article.p.text
        print(summary)

head_and_summary(articles)