from dataclasses import dataclass


@dataclass
class Vector3D:
    x: int
    y: int
    z: int

    def __post_init__(self):
        self.length = (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


if __name__ == "__main__":
    vector = Vector3D(1, 2, 3)
    print(vector, vector.length)
    print(vector.__dict__)
