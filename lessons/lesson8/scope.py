_x = 5


def scope():
    x = 10
    print(x)


def scout_2():
    print(f'innter scout {x}')

    scout_2()


scope()
scout_2()