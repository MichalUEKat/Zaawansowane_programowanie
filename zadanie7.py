import requests
import json


class Brewery:
    def __init__(self, id: str, name: str, brewery_type: str) -> None:
        self.id = id
        self.name = name
        self.brewery_type = brewery_type

    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.brewery_type}"


def map_to_obj_list(brewery_list: list[dict]) -> list[Brewery]:
    brewery_obj_list = []
    for element in brewery_list:
        b = Brewery(element["id"], element["name"], element["brewery_type"])
        brewery_obj_list.append(b)
    return brewery_obj_list


response = requests.get(url="https://api.openbrewerydb.org/breweries?per_page=20")
json_dict = response.json()
object_list = map_to_obj_list(json_dict)

for brewery in object_list:
    print(brewery.__str__())
