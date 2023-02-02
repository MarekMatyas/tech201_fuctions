def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def multiply(a: int, b: int) -> float:
    return a * b

def divide(a: int, b: int) -> float:
    return a / b

number_one = float(input("Enter the first number:"))
number_two = float(input("Enter the second number:"))

user_choice = input("What calculation is desired? ('add', 'sub', 'multi', 'div'):")
if user_choice == "add":
    print(add(number_one, number_two))
elif user_choice == "sub":
    print(subtract(number_one, number_two))
elif user_choice == "multi":
    print(multiply(number_one, number_two))
elif user_choice == "div":
    print(divide(number_one, number_two))
else:
    print("Wrong calculation, please try again")
