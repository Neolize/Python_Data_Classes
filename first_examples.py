from typing import Union
from dataclasses import dataclass


class Toy:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"Toy: name: {self.name}, weight: {self.weight}, price: {self.price}"


@dataclass
class ToyData:
    name: str = "Nameless"
    weight: Union[float, int] = 0
    price: float = 0.0


if __name__ == "__main__":
    toy = Toy("Hedgehog", 0.7, 500.0)
    toy_data = ToyData("Soldier", 1.1, 1200.0)
    toy_without_data = ToyData()
    print(toy, toy_data, toy_without_data, sep="\n")
