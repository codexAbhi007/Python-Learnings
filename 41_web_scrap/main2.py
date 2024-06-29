from bs4 import BeautifulSoup
import requests
import csv

r = requests.get('https://books.toscrape.com/catalogue/category/books/horror_31/index.html').text
with open(r'41_web_scrap\horror.csv','a')as fc:
    writer = csv.writer(fc)
    header = ['Title','Price']
    writer.writerow(header)
    soup = BeautifulSoup(r,'lxml')

    # print(soup.prettify())

    # section = soup.section.find_all('div')[1].ol.li.article.h3.a.text
    article = soup.find('article',class_="product_pod")
    title = article.h3.a.text
    price = article.find('div',class_='product_price').p.text
    # print(article)
    # print(title)
    # print(price)


    ol = soup.find_all('ol',class_='row')[0]
    # print(ol)


    li = soup.find_all('li',class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')
    for i in li:
        title = i.article.h3.a.text
        price = i.article.find('div',class_='product_price').p.text
        # print("Title: ",title)
        # print("Price: ",price,'\n')
        writer.writerow([title,price])
    
    print('Done!')
