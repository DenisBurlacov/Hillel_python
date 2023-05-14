a = 30
b = 50
c = int(input("Please enter a num "))

if a < b:
    print(f'{b} greater than {a}')

# =================================================
if a > b:
    print(f'{a} greater than {b}')
else:
    print(f'{b} greater than {a}')

# =================================================
if c >= a:
    print(f'{c} / {a} =', c / a)
elif c <= a and c != 0:
    print(f'{a} / {c} =', a / c)
elif c == 0:
    print("Exception, you can't divide on zero")

if c == a:
    print(f'Entered num {c} = variable {a}')

if c != a:
    print(f'Entered num {c} not equal variable {a}')

# ===================================================
