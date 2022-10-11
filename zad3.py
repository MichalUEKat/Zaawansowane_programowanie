# Stworzyć funkcję, która będzie sprawdzała czy przekazana liczba w parametrze jest
# parzysta i zwróci tą informację jako typ logiczny bool ( True / False ). Należy
# uruchomić funkcję, wynik wykonania zapisać do zmiennej, a następnie
# wykorzystując warunek logiczny wyświetlić prawidłowy tekst "Liczba parzysta" /
# "Liczba nieparzysta"

def isEven(number:int)->bool:
    return number%2==0

result = isEven(9)
if(result):
    print("Parzysta")
else:
    print("Nieparzysta")

