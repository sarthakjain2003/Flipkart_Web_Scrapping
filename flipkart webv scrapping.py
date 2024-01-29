import pandas as pd
import requests
from bs4 import BeautifulSoup

product_name = []
price = []
review = []
description = []

for i in range(2,12):
    url = "https://www.flipkart.com"
    url1 = "https://www.flipkart.com/search?q=mobile+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_16_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_16_na_na_na&as-pos=3&as-type=RECENT&suggestionId=mobile+under+50000&requestId=e9c7586e-8850-4a7a-962b-9fa1c90fff27&as-searchtext=mobile+under+50000&page="+str(i)
    r = requests.get(url)
# print(r)

    r1 = requests.get(url1)

    soup = BeautifulSoup(r1.text, "lxml")
    box = soup.find("div", class_ = "_1YokD2 _3Mn1Gg")
# print(soup)

    names = box.find_all("div", class_="_4rR01T")
    for i in names:
      name = i.text
      product_name.append(name)

# print(product_name)

    prices = box.find_all("div", class_="_30jeq3 _1_WHN1")
    for i in prices:
        price_ = i.text
        price.append(price_)
# print(price)

    reviews = box.find_all("div", class_="_3LWZlK")
    for i in reviews:
       reviews_ = i.text
       review.append(reviews_)
# print(review)

    descriptions = box.find_all("ul", class_="_1xgFaf")
    for i in descriptions:
        description_ = i.text
        description.append(description_)
# print(description)
# print(names)
                                                                                                                                
df = pd.DataFrame({"Product Name": product_name, "Price": price, "Review": review, "Description": description})
print(df)

df.to_csv("E:/sarthak/college work/internship/data analytics/flipkart.csv")

# while True: 
# np = soup.find("a", class_ = "_1LKTO3").get("href")
#cnp = "https://www.flipkart.com"+np
# print(cnp)

# url2 = cnp
# r2 = requests.get(url2)
# soup1 = BeautifulSoup(r2.text, "lxml")
# print(soup1)



