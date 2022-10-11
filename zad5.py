# Stworzyć funkcję, która przyjmie 2 argumenty. Pierwszy typu list , a drugi typu int
# . Funkcja ma sprawdzić (zwracając typ logiczny bool ), czy lista z parametru
# pierwszego zawiera taką wartość jaką przekazano w parametrze drugim.

def contains_search_value(sample_list:list[int],search:int):
    return search in sample_list

print(contains_search_value([2,3,4,5],2))