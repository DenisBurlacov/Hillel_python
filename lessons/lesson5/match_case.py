var = "Denis"

if var == '':
    pass
elif var == 'a':
    pass
else:
    print("Cant do anything")

match var:
    case 'Denis':
        pass
    case 'test':
        pass
    case 123:
        print('finish')
