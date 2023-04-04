def custom_factorial(num: int) -> int:
    if num <= 0:
        return 0

    total = 1
    for item in range(1, num + 1):
        total *= item

    return total


if __name__ == "__main__":
    number = ""

    while number.isdigit() is False:
        number = input("Enter a number to calculate a factorial: ")

    print(f"Factorial of {number} is {custom_factorial(int(number))}")
    print(f"A sequence of factorials of the given number: "
          f"{', '.join(str(custom_factorial(item)) for item in range(1, int(number) + 1))}")
