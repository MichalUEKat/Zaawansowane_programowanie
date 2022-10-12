import requests
import json
from types import SimpleNamespace

class Beer:
    def __init__(self,id,name,brewery_type):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type

    def print(self):
        print(f"{id}; {name}; {brewery_type};")

Url= "https://api.openbrewerydb.org/breweries";
r= requests.get(Url)
data = r.json()

beers:list[Beer]=[]
for element in data:
    id = element['id']
    name= element['name']
    brewery_type = element['brewery_type']
    print(f"{id},{name},{brewery_type}")
    beers.append(Beer(id,name,brewery_type))

print("******************************************")
for b in beers:
    b.print()
