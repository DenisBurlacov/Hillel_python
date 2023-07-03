try:
    with open('output.csv', 'x') as f:
        f.read()


except ZeroDivisionError as zero:
    print(f'This is zero division error: {zero}')

except ArithmeticError as ae:
    print(f'ArithmeticError: {ae}')


except Exception as ex:
    print(f'Something went wrong: {ex}')

else:
    print('test')

finally:
    print('This block is always run')
