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

number_one = float(input("Enter the first number:"))
#This line of code will ask for the user to input the first number
number_two = float(input("Enter the second number:"))
# This line asks for the second number

user_choice = input("What calculation is desired? ('add', 'sub', 'multi', 'div'):")
#This line of code with ask the user to choose a calculation method


if user_choice == "add": # This line opens an if statement stating if users choice is "add" then:
    print(add(number_one, number_two)) #  prints out the output using the function above
elif user_choice == "sub":
    print(subtract(number_one, number_two))
elif user_choice == "multi":
    print(multiply(number_one, number_two))
elif user_choice == "div":
    print(divide(number_one, number_two))
else:
    print("Wrong calculation, please try again")# If user input wrong calculation method this message will print out.
