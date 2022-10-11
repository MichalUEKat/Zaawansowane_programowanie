# Stworzyć funkcję, która przyjmie 3 argumenty typu int i sprawdzi czy suma dwóch
# pierwszych liczb jest większa lub równa trzeciej, a następnie zwróci tę informację
# jako typ logiczny bool


def zad4(n1:int,n2:int,n3:int)->bool:
    return (n1+n2)>=n3

print(zad4(1,2,3))