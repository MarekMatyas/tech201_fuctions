def add(a: int, b: int) -> float:
    return a + b
# First we define function called "add" with arguments (a, b) and return statement to return the value
def subtract(a: int, b: int) -> float:
    return a - b
# Same goes with all the other arithmetic functions
def multiply(a: int, b: int) -> float:
    return a * b

def divide(a: int, b: int) -> float:
    return a / b

def convert(a: int,) -> float:
    return a * 0.01




user_choice = input("What calculation is desired? ('add', 'sub', 'multi', 'div', 'conv'):")

if user_choice == "conv":
    convert_choice = float(input("Please enter the number you want to convert in meters: "))
    print(convert(convert_choice))
    print(convert_choice * 3.28084)
else:
    number_one = float(input("Enter the first number:"))
    number_two = float(input("Enter the second number:"))
    if user_choice == "add":  # This line opens an if statement stating if users choice is "add" then:
        print(add(number_one, number_two))  # prints out the output using the function above
    elif user_choice == "sub":
        print(subtract(number_one, number_two))
    elif user_choice == "multi":
        print(multiply(number_one, number_two))
    elif user_choice == "div":
        print(divide(number_one, number_two))
    else:
        print("Wrong calculation, please try again")  # If user input wrong calculation method this message will print out.


