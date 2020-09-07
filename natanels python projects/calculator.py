print (" welcome to the calculator times = *  plus = +  minus = -  and  divided = / ")
num1 = float(input("enter first number: "))
operator = input("enter operator: ")
num2 = float(input("enter second number: "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "/":
    print(num1 / num2)
elif operator == "*":
    print(num1* num2)
else:
    print ("invalid operator")

