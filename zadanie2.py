
import statistics


class Student:
    def __init__(self,name:str, marks:list[int]) -> None:
        self.name = name
        self.marks= marks
    def is_passed(self):
        number_mean = statistics.mean(self.marks)
        if(number_mean>50):
            return True
        return False
    def __str__(self) -> str:
        marks_list = [str(x) for x in self.marks]
        marks_str= ','.join(marks_list)

        return f'Student: {self.name}: {marks_str}'

class Library:
    def __init__(self,
    city:str,
    street:str,
    zip_code:str,
    open_hours:str,
    phone:str,
    ) -> None:
        self.city= city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone
    def __str__(self) -> str:
        return f"Biblioteka: {self.city} {self.street} {self.zip_code} {self.open_hours} {self.phone}"

class Employee:
    def __init__(self,first_name:str, last_name:str, hire_date:str, birth_date:str, city:str, street:str, zip_code:str, phone:str) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date =birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self) -> str:
        return f"Pracownik: {self.first_name} {self.last_name} {self.hire_date} {self.birth_date} {self.city} {self.street} {self.zip_code} {self.phone}"
class Book:
    def __init__(self, library:Library,publication_date:str,author_name:str,author_surname:str, number_of_pages:str) -> None:
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self) -> str:
        return f"Książka: {self.library} {self.publication_date} {self.author_name} {self.author_surname} {self.number_of_pages}"

class Order:
    def __init__(self,employee:Employee,student:Student,books:list[Book],order_date:str) -> None:
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date
    def __str__(self) -> str:
        books_list = [x.__str__() for x in self.books]
        books_str = '\n'.join(books_list)
        # print(books_str)
        return f"\nZamówienie: {self.employee.__str__()}\n{self.student.__str__()}\n{books_str}\n{self.order_date}"
# Dodatkowo:
# Każda klasa ma mieć zaimplementowaną metodę __str__ , która będzie opisywała obiekt oraz ewentualne obiekty
# znajdujące się w tym obiekcie (np. obiekt Library w obiekcie Book).
# Pola w klasie mają być zdefiniowane jako atrybuty ustawiane podczas tworzenia instancji klasy za pośrednictwem
# konstruktora.
# Stworzyć 2 biblioteki (2 instancje klasy), 5 książek, 3 pracowników, 3 studentów, oraz 2 zamówienia.
# Wyświetlić oba zamówienia ( print )

student = Student("Romuald",[2,2,2,2,2,2,3,3,3,3])

library1= Library("Katowice","Ulica 1","44-000","24/7","997")
library2 = Library("Rybnik", "Kościuszki","44-200","8-9","123321123")

book1 = Book(library1,"2021","Jarosław","Kaczkowski",231)
book2 = Book(library2, "1999","Jan","Kowalski",543)
book3 = Book(library1, "1999","Jan","Kowalski",123)
book4 = Book(library2, "1999","Jan","Kowalski",4321)
book5 = Book(library1, "1999","Jan","Kowalski",123)

employee1 = Employee("Jan","Robotnik",1993,"01.10.1970","Katowice","Wypoczynkowa 12","231","78321312")
employee2 = Employee("Paweł","Robotnik",1993,"01.10.1970","Katowice","Wypoczynkowa 12","231","78321312")
employee3 = Employee("Robert","Robotnik",1993,"01.10.1970","Katowice","Wypoczynkowa 12","231","78321312")

order1 = Order(employee1,student,[book1,book3,book4],"1.10.2022")
order2 = Order(employee2,student,[book2,book3,book5],"1.1.2022")

print(order1.__str__())
print(order2.__str__())
