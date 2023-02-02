# tech201_functions

## Introducion to functions 

**Function is a block of code which only runs when it's called.**
You can pass data, known as arguments. 
## D R Y (***Don't Repeat Yourself***)

Let's create a functions for quick example:

``` 
def print_something():
print("Something has been printed")
print_something()
```
Function has to be called outside of the function.
The word `def` is a key word (define).

### Functions and arguments

``` 
def print_something(print_string): 
    print(print_string)
```
As we can see in this example nothing will happen because we haven't actually called the function yet.

``` 
print_something("This is my variable")
print_something("This is the second one ")
```
Once we called the function anywhere throughout the code, we will get our output depending on the arguments set in place.

### ***Another very useful example:***

``` 
def greetings(name):
    print("Hello, my name is " + name )

greetings("Luke")
greetings("Marek")
greetings("Waleed")
```
In this code we can clearly see that when we call our function, we can pass an argument to be connected and printed with a string `"Hello, my name is "`


## The `return` statement
The python return statement is a special statement that you can use inside a function to send a functions result back to the caller.

In other words, the `return` statement is used to end the execution of the function call and returns the result( value of the expression following the return keyword)to the caller.

If the return statement is without any expression, then the special value `None` is returned.

A ***return statement*** is overall used to invoke a function so that the passed statements can be executed.

### Quick example of `return` statement
``` 
def addition(int1, int2):
    return int1 + int2

print(addition(2 ,2 ))
```
This function will return the addition of passed arguments, in this case 4.


## Default arguments

The default arguments in Python **represents the function arguments that will be used if no arguments are passed when the function is called**

### Quick example
``` 
def addition(int1=2, int2= 2):
    return int1 + int2


print(addition())
```
In this  case we don't need to specify the arguments because we defined it in the definition.

```
def addition(int1=2, int2= 2):
    return int1 + int2 

print(addition(10, 10))
```
We can also overwrite the arguments, but if we try to call the function again without any arguments, the function will go with what was set as a default argument.