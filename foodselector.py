
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

def restaurants_filter(args, restaurants):

    filtered = []
    for r in restaurants:
        if ((args.type == "all" or args.type in r.foodtype) and
            (args.diet == "all" or args.diet in r.diet)
            ):

            filtered.append(r)

    return filtered


class Restaurant:

    def __init__(self, name, foodtype, diet):

        self.name = name
        self.foodtype = foodtype
        self.diet = diet


    def __str__(self):
        rep = "{} - Type of food {} - Diet {} ".format(self.name, self.foodtype, self.diet)
        return rep

parser = argparse.ArgumentParser(description='You automatic randomized food selector to avoid delays when selecting a restaurant for delivery')
parser.add_argument("--restaurants","-r", type=str, default="The file containing your favourite restaurants and and their relevant information (see corunna.txt as an example")
parser.add_argument('--type', "-t", type=str, default="all", help='Specify the type of food you want')
parser.add_argument('--diet', "-d", dest='diet', default="all", help="")

args = parser.parse_args()

restaurants = data_reader("restaurants/corunna.json")
restaurants_filtered = restaurants_filter(args, restaurants)
print ("------------------------------------------")
print ("Restaurant options ({})".format(len(restaurants_filtered)))
print ("------------------------------------------")
for r in restaurants_filtered:
    print (r)
print("\n\n")
r = random.choice(restaurants_filtered)
print ("------------------------------------------")
print ("The selected restaurant is:\n")
print (r)
print ("------------------------------------------")