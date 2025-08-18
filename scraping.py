import requests
from bs4 import BeautifulSoup

url = "https://sneakerstore.by/muzhskie-krossovki/"

response = requests.get(url)
soup = BeautifulSoup(response.text,features="html.parser")
