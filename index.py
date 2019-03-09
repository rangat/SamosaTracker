import requests
import pprint as p
import json

menu = requests.get('https://rumobile.rutgers.edu/1/rutgers-dining.txt').json()



# 0 to 3, 0 being brower, 1 being busch, 2 being livi, 3 being cook

for spec_dict in menu:
    # iterate through x
    
    if type(x) == list:
        print("it's a list!")
        # iterate more
    elif type(x) == dict:
        for key, value in x:

        print("it's a dict")
    
    continue    
