class Property:
    def __init__(self, area: str, rooms: int, price: float, address: str) -> None:
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self) -> str:
        return f"{self.area} {self.rooms} " f"{self.price} {self.address}"


class House(Property):
    def __init__(
        self, area: str, rooms: int, price: float, address: str, plot: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self) -> str:
        return super().__str__() + f" {self.plot}"


class Flat(Property):
    def __init__(
        self, area: str, rooms: int, price: float, address: str, floor: int
    ) -> None:
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self) -> str:
        return super().__str__() + f" {self.floor}"


house = House("Rybnik", 10, 800000, "Dozynkowa", 100000)
flat = Flat("Tychy", 1, 100000, "Tyska 25", 5)

print(house.__str__())
print(flat.__str__())
