def adding(int1, number_two):
    return int1 + number_two
def subtracting(int1, number_two):
    return int1 - number_two
def dividing(int1, number_two):
    return int1 / number_two
def mupltiplying(int1, number_two):
    return int1 * number_two

int1= 5
number_two= 5

add_total= adding(int1, number_two)
sub_total= subtracting(number_one, number_two)
div_total= dividing(number_one, number_two)
multi_total= mupltiplying(number_one, number_two)

print(f"Addition= " + add_total)
print(f"Subtraction= " + sub_total)
print(f"Division= " + div_total)
print(f"Multiplication= " + multi_total)
