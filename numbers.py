from math import factorial as fact


if __name__ == "__main__":
    number = ""

    while number.isdigit() is False:
        number = input("Enter a number to calculate the factorial: ")

    print(f"Factorial of {number} is {fact(int(number))}")
    print(f"The square of {number} is {int(number) ** 2}")
