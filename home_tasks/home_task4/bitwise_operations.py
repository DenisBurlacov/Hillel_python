# Побітові операції:
# побітове AND:
# Порівняти два різних цілих і два однакових числа і вивести результат
a = 5
b = 12
print(a & a)
print(a & b)

# Порівняти два різних рядка і два однакових рядка і вивести результат
# The & operator yields the bitwise AND of its arguments, which must be integers or
# one of them must be a custom object overriding __and__() or __rand__() special methods.
#
# The ^ operator yields the bitwise XOR (exclusive OR) of its arguments, which must be integers
# or one of them must be a custom object overriding __xor__() or __rxor__() special methods.
#
# The | operator yields the bitwise (inclusive) OR of its arguments, which must be integers or
# one of them must be a custom object overriding __or__() or __ror__() special methods.

c = 0b0110
d = 0b0101
print(c & c)
print(c & d)

# Повторити дії і та іі з пункту а для решти операцій (OR, XOR, NOT)

print(a | a)
print(a | b)
print(a ^ a)
print(a ^ b)
print(a ^ ~ a)
print(a ^ ~ b)

print(c | c)
print(c | d)
print(c ^ c)
print(c ^ d)
print(c ^ ~ c)
print(c ^ ~ d)

# Виконати побітовий зсув вліво для:
# Цілого числа на 1, 2 та 3 біти
# Рядка на 1, 2 та 3 біти

a = a << 1
print(a)
a = a << 2
print(a)
a <<= 3
print(a)

# string = 'string'
# res = string << 'sl'
# print(res)
# в данном случае TypeError: unsupported operand type(s) for <<: 'str' and 'str'



# Виконати побітовий зсув вправо для:
# Цілого числа на 1, 2 та 3 біти
# Рядка на 1, 2 та 3 біти
b = a >> 1
print(b)
a = a >> 2
print(a)
a >>= 3
print(a)