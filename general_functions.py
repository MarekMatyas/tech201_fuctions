Functions are a tool

D R Y # Don't Repeat Yourself
Create a function

def print_something(): ## def... is a key word define ##print_something is the name of the fuctions and () are for the arguments
    print("Something has been printed")

print_something()         # the functions has to be called outside of the functions






# Functions and arguments

def print_something(print_string): ### Naming the arguments properly is really important
    print(print_string)

print_something("This is my variable")

print_something("This is the second one ") # We can call the function made anywhere throughout the code


In strong type language like JAVA
public void print_string(string_text)


def greetings(name):
    print("Hello, my name is " + name )

greetings("Luke")
greetings("Marek")
greetings("Waleed")


# The return statement- The python return statement is a special statement that you can use inside a function
# to send a functions result back to the caller.


def addition(int1, int2):
    return int1 + int2

print(addition(2 ,2 ))


Default arguments

def addition(int1=2, int2= 2):
    return int1 + int2

print(addition()) # in this case we don't need to specify the arguments here because we defined it in the definition
print(addition(10, 10)) ## the arguments can be overwritten
print(addition()) ## the arguments will stay default if not overwritten


# Multiple arguments

def multi_args(*multiargs): ##    it will take as many arguments as we want
    print(type(multiargs))

    for arg  in multiargs:
        print(arg)

multi_args(1, 2, 3, 4, 5, 6)


# ## Type Hints
#
def greeting(name: int):    # type hint. to ensure that the same data type is used
    print("Hello, my name is :" + name)

#
# greeting(343)

def division(num1: int = 5, num2: int = 2) -> float:   ##<class 'float'> this is the input
    return num1 / num2
print(division())


## Function best practices

## Name your functions clearly using lower case and underscores
## All arguments should be clear in their need and where possible include the expected type
## Remember return statement or your function will return None
## Keep functions small for readability and simplicity
## Use comments in your functions/methods to give instructions on how to use them
## Consider using Type Hints to avoid type errors when you run your code.






