class Toy:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def __str__(self):
        return f"Toy: name: {self.name}, weight: {self.weight}, price: {self.price}"


if __name__ == "__main__":
    toy = Toy("Hedgehog", 0.7, 500)
    print(toy)
