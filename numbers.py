from math import factorial as fact


if __name__ == "__main__":
    number = ""

    while number.isdigit() is False:
        number = input("Enter a number to calculate a factorial: ")

    print(f"Factorial of {number} is {fact(int(number))}")
    print(f"A sequence of factorials of the given number: "
          f"{', '.join(str(fact(item)) for item in range(1, int(number) + 1))}")
