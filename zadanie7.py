import requests
import json
# Dla chętnych Stworzyć skrypt pythonowy, który połączy się z API, które zawiera
# informacje o browarach (dokumentacja
# https://www.openbrewerydb.org/documentation).
# Należy w pythonie zrobić klasę Brawery , która będzie zawierała takie atrybuty jakich
# dostarcza API wraz z odpowiednim typowaniem.
# W klasie należy zaimplementować magiczną metodę __str__ która będzie
# opisywała dane przechowywane w obiekcie.
# Skrypt ma się połączyć do API i pobrać 20 pierwszych obiektów, a następnie
# utworzyć listę 20 instancji klasy Brawery , którą przeiteruje i wyświetli każdy obiekt z
# osobna.

class Brewery:
    def __init__(self, id:str, name:str, brewery_type:str) -> None:
        self.id = id
        self.name= name
        self.brewery_type = brewery_type
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.brewery_type}"

def map_to_obj_list(brewery_list:list[dict])->list[Brewery]:
    brewery_obj_list = []
    for element in brewery_list:
        b= Brewery(element['id'],element['name'], element['brewery_type'])
        brewery_obj_list.append(b)
    return brewery_obj_list

response = requests.get(url="https://api.openbrewerydb.org/breweries?per_page=20")
json_dict = response.json()
object_list =map_to_obj_list(json_dict)

for brewery in object_list:
    print(brewery.__str__())











# "id": "10-56-brewing-company-knox",
#         "name": "10-56 Brewing Company",
#         "brewery_type": "micro",
#         "street": "400 Brown Cir",
#         "address_2": null,
#         "address_3": null,
#         "city": "Knox",
#         "state": "Indiana",
#         "county_province": null,
#         "postal_code": "46534",
#         "country": "United States",
#         "longitude": "-86.627954",
#         "latitude": "41.289715",
#         "phone": "6308165790",
#         "website_url": null,
#         "updated_at": "2022-08-20T02:56:08.975Z",
#         "created_at": "2022-08-20T02:56:08.975Z"



