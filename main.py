num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
sign = input("Enter the sign: ")

def calculate(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    elif sign == '-':
        return num1 - num2
    elif sign == '*':
        return num1 * num2
    elif sign == '/':
        return num1 / num2
    else:
        return 'Error'

result = calculate(num1, num2, sign)
print(f"{num1} {sign} {num2} = {result}")
