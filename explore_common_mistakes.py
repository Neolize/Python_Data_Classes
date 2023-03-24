from typing import Optional


def add_number_to_array(number: int, arr: Optional[list] = None) -> list:
    arr = arr or []
    arr.append(number)
    return arr


if __name__ == "__main__":
    for item in range(10, 14):
        if item < 13:
            print(add_number_to_array(item))
        else:
            print(add_number_to_array(item, [55, 77]))
