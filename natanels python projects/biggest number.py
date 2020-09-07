
def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

one = input("enter in a number:")
two = input("enter a second number:")
three = input("enter in a third number:")
float(three)
float(two)
float(one)

print(max_num(one,two,three))