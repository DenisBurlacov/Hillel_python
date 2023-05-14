a = int(input("Enter first num"))
b = int(input("Enter second num"))
operator = input("Enter operator, + or - or * or /")

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    if b == 0:
        print("Isn't possible divide on zero!")
    else:
        print(a / b)
else:
    print("Operation isn't correct")