import csv

def add_to_csv(scrap):
    FILENAME = "shoes.csv"

    with open(FILENAME,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerows(scrap())
