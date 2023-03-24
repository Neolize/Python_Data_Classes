from dataclasses import dataclass, field


@dataclass
class Vector3D:
    x: int
    y: int
    z: int = field(compare=False)
    length: float = field(init=False, repr=False, compare=False)

    def __post_init__(self):
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def compare_lengths(self, other_vector: 'Vector3D') -> str:
        if self.length == other_vector.length:
            return "Lengths are equal"
        return "Lengths aren't equal."


if __name__ == "__main__":
    first_vector = Vector3D(3, 6, 5)
    second_vector = Vector3D(3, 6, 2)

    print(f"{first_vector}, length={first_vector.length}")
    print(f"{second_vector}, length={second_vector.length}")

    print(first_vector == second_vector)
    print(first_vector.compare_lengths(second_vector))
