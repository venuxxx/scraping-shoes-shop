import json

def add_to_json(scrap):
    FILENAME = "../result scraping/shoes.json"

    with open(FILENAME,"w",newline="") as file:
        for name,price in scrap():
            json.dump({name:{"price":price}},file)
