
import argparse
import json
import random


def data_reader(path):
    restaurants = []

    with open(path) as json_file:
        data = json.load(json_file)

    for r in data["restaurants"]:
        restaurants.append(Restaurant(r["name"],r["type"], r["diet"]))

    return restaurants

class Restaurant:

    def __init__(self, name, foodtype, diet):

        self.name = name
        self.foodtype = foodtype
        self.diet = diet


parser = argparse.ArgumentParser(description='You automatic randomized food selector to avoid delays when selecting a restaurant for delivery')
parser.add_argument("--restaurants","-r", type=str, default="The file containing your favourite restaurants and and their relevant information (see corunna.txt as an example")
parser.add_argument('--type', "-t", type=str, default="type", help='Specify the type of food you want')
parser.add_argument('--diet', "-d", dest='diet', default="none", help="")


restaurants = data_reader("restaurants/corunna.json")

r = random.choice(restaurants)
print ("Restaurant: {}. Type of food {}. Diet {} ".format(r.name, r.foodtype, r.diet))