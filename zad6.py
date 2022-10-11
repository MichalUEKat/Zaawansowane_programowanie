# Stworzyć funkcję, która przyjmuje 2 argumenty typu list i zwraca wynik typu list .
# Funkcja ma za zadanie złączyć przekazane listy w jedną, usunąć duplikaty, każdy
# element podnieść do potęgi 3 stopnia, a następnie zwrócić powstałą listę.
import math

def zad6(sample_list_1:list[int], sample_list_2:list[int])->list[int]:
    result_list=sample_list_1+sample_list_2
    result_list = list(dict.fromkeys(result_list))
    result_list =[x**3 for x in result_list]
    return result_list

print(zad6([2,3,4,5,5,1],[9,8,7,5,7,8]))