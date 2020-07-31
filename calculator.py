#Variables
num1 = input("Choose a number: ")
num2 = input("Choose a number: ")
operator = input("Select which operator you would like to use or type help to display a list of operators and their functions: ")
#help = input("Type help to display a list of operators and their functions")
add = float(num1) + float(num2)
sub = float(num1) - float(num2)
mult = float(num1) * float(num2)
div = float(num1) / float(num2)
operator.l = [("+"),("-"), ("*"), ("/"), ("help").lower]
X = "+: Adds, -: Subtracts, *: Multiplies, /: Divides"
while operator.l == [("+"),("-"), ("*"), ("/"), ("help").lower]:
    if operator == ("+"):
    print(add)
    elif operator == ("-"):
    print(sub)
    elif operator == ("*"):
    print(mult)
    elif operator == ("/"):
    print(div)
    elif operator == ("help").lower():
    print(X)

#   print("Invalid input, please try again")

