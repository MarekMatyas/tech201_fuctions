## Instructions on calculator using functions

First we define a function call `add` with arguments (a, b) and return statement to return the value.
``` 
def add(a: int, b: int) -> float:
    return a + b
```
Same goes with all the other arithmetic method.
``` 
def subtract(a: int, b: int) -> float:
    return a - b
    
def multiply(a: int, b: int) -> float:
    return a * b
    
def divide(a: int, b: int) -> float:
    return a / b
    
def convert(a: int,) -> float:
    return a * 0.01
```

Then we need to create a variable (user_choice) with the input giving the user a choice (add, sub, multi, div, conv).
``` 
user_choice = input("What calculation is desired? ('add', 'sub', 'multi', 'div', 'conv'):")
```

After that we will need to state the conditions to work with the user's input.

