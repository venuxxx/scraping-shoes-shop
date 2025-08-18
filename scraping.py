import requests
from bs4 import BeautifulSoup
import excelmodule
from time import sleep

def check_product():
    url = "https://sneakerstore.by/muzhskie-krossovki/"
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:141.0) Gecko/20100101 Firefox/141.0"}

    response = requests.get(url,headers = headers)
    soup = BeautifulSoup(response.text, features="html.parser")

    page = 1
    MAX_PRICE = 150
    products = soup.find_all("li", class_="catalogue__products-list-item")

    while len(products) != 0:
        for product in products:
            price = int(product.find_all("span",class_= "catalogue__price catalogue__price--sm")[-1].text.split(".")[0])
            if price<=MAX_PRICE:
                name = product.find("a",class_="catalogue__product-name products-list__name").find("span").text
                yield name,price
        page += 1
        response = requests.get(url + f"?page={page}",headers=headers)
        soup = BeautifulSoup(response.text, features="html.parser")
        products = soup.find_all("li", class_="catalogue__products-list-item")

excelmodule.add_to_excel(check_product)