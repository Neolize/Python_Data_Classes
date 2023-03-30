from typing import Union
from dataclasses import dataclass, field


class Toy:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"Toy: name: {self.name}, weight: {self.weight}, price: {self.price}"


@dataclass(order=True)
class ToyData:
    name: str = field(compare=False, default="Nameless")
    weight: Union[float, int] = field(compare=False, default=0)
    price: float = 0.0
    materials: list = field(compare=False, default_factory=list)


if __name__ == "__main__":
    toy = Toy("Hedgehog", 0.7, 500.0)
    toy_data = ToyData("Soldier", 1.1, 1200.0)
    toy_data.materials.append("iron")
    toy_without_data = ToyData()
    print(toy, toy_data, toy_without_data, sep="\n")

    print(toy_data > toy_without_data)
    toy_without_data.price = 1500.0
    print(f"Toy data: {toy_data.price}, toy without data: {toy_without_data.price}")
    print(toy_data > toy_without_data, toy_data == toy_without_data, toy_data < toy_without_data)
