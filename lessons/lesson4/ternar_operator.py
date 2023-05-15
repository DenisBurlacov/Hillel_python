# ternar operator

name = "Den"
if name == "Den":
    print(name)

base = 4
new_var = None

if base % 2 == 0:
    new_var = True
    if base < 5:
        print("base is lees then 6")
    else:
        print("base is greater then 5")
else:
    new_var = False

print("The number {} is even:".format(base, new_var))

ternary_var = True if base % 2 == 0 else False

print("The number {} is even:".format(base, new_var))