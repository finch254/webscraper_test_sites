import requests

import pandas as pd
from bs4 import BeautifulSoup


url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")

names = soup.find_all("a", class_="title")
product_name = []
for i in names:
    name = i.text
    product_name.append(name)
# print(product_name)

prices = soup.find_all("h4", class_="pull-right price")
prices_list = []
for i in prices:
    price = i.text
    prices_list.append(price)
# print(prices_list)

desc = soup.find_all("p", class_="description")
product_description = []
for i in desc:
    description = i.text
    product_description.append(description)
# print(product_description)

review = soup.find_all("p", class_="pull-right")
review_list = []
for i in review:
    reviews = i.text
    review_list.append(reviews)
# print(review_list)

df = pd.DataFrame({"Product Name": product_name, "Price List": prices_list, "Product Description": product_description,
                   "Reviews": review_list})
# print(df)

df.to_csv("finch0001.csv")
