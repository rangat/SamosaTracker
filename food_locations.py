import requests
import pprint as p
import json
import Levenshtein as l

menu = None
menu = requests.get('https://rumobile.rutgers.edu/1/rutgers-dining.txt').json()

# with open('new_json.json', 'w') as j:
#     json.dump(menu, j)

# with open('menu_example.json', 'r') as m:
#     menu = json.load(m)

# 0 to 3, 0 being brower, 1 being busch, 2 being livi, 3 being cook

def get_location_of_food(json:dict, food:str)->list:
    meal_locations = []
    for dinning_hall in json:
        if dinning_hall.get('meals'):
            for meal in dinning_hall.get('meals'):
                if meal.get('genres'):
                    for genre in meal.get('genres'):
                        if genre.get('items'):
                            for item in genre.get('items'):
                                # add logic here for some similarity function:
                                # Cosine similarity, Jaccard similarity, or Levenshtein distance
                                if l.distance(food, item) < 4:
                                    meal_locations.append((item, meal['meal_name'], dinning_hall['location_name']))
    return meal_locations

p.pprint(get_location_of_food(menu, "Samosa"))
