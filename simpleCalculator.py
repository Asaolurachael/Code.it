
num1 = int(input('> '))                 # input first number and cast to int
num2 = int(input('> '))                 # input second number and cast to int
operand = input('Enter Operand: ')        # input operand

# If else statement to determine operand
if operand == '+':
    result = num1 + num2
elif operand == '-':
    result = num1 - num2
elif operand == '/':
    result = num1 / num2
elif operand == '*':
    result = num1 * num2

print(result)


