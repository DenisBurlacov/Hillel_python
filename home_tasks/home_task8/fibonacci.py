def fibonacci(num):
    if num in {0, 1}:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fibonacci_values(num):
    for i in range(num):
        print(fibonacci(i), end=' ')


fibonacci_num = int(input('Please enter a number to show fibonacci row '))
fibonacci_values(fibonacci_num)
