from typing import Union
from dataclasses import dataclass, field, InitVar


@dataclass(order=True)
class Vector3D:
    x: int
    y: int
    z: int = field(compare=False)
    calc_length: InitVar[bool] = True
    length: float = field(init=False, repr=False, compare=False, default=0)

    def __post_init__(self, calc_length: bool) -> None:
        if calc_length:
            self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def recalculate_length(self) -> None:
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def compare_lengths(self, other_vector: 'Vector3D') -> str:
        if self.length == other_vector.length:
            return "Lengths are equal"
        return "Lengths aren't equal."

    def multiply_length_by_given_number(self, number: int) -> Union[int, float]:
        if not isinstance(number, int):
            print(f"The function may accept only integer numbers but got {type(number)} instead")
            return 0
        return self.length * number


if __name__ == "__main__":
    first_vector = Vector3D(3, 6, 5)
    second_vector = Vector3D(3, 6, 2)
    third_vector = Vector3D(10, 6, 7, calc_length=False)

    print(f"{first_vector}, length={first_vector.length}")
    print(f"{second_vector}, length={second_vector.length}")
    print(f"{third_vector}, length={third_vector.length}")

    print(first_vector == second_vector)
    print(second_vector > third_vector)
    print(first_vector.compare_lengths(second_vector))
    print(f"New length: {second_vector.multiply_length_by_given_number(7)}")

    print(first_vector.x)
    print(first_vector.length)
    first_vector.x = 10
    first_vector.recalculate_length()
    print(first_vector.x)
    print(first_vector.length)
