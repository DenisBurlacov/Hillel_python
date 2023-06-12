def multiply(x, y):
    return print(x * y)


multiply(2, 2)

mult = lambda x, y: print(x * y)

mult(3, 3)

lamd_da = lambda x, y, func: func(x, y)

lamd_da(2, 3, mult)
lamd_da(2, 3, multiply)

_lamda = lambda x, y: print(f'My full name is: {x} {y}')

_lamda('Denis', 3)

format_numeric = lambda num: f"{num:e}" if isinstance(num, int) else f"{num:.2f}"

print("int fromating:", format_numeric(10000000))
print("float fromating:", format_numeric(999999999.92349598234))