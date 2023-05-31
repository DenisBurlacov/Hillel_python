def season(month_num):
    if month_num == 12 or month_num < 3:
        return 'Winter'
    elif month_num == 3 or month_num < 6:
        return 'Spring'
    elif month_num == 6 or month_num < 9:
        return 'Summer'
    else:
        return 'Autumn'


_num_month = int(input('Please enter the num of season '))

if _num_month <= 0 or _num_month > 12:
    print("The entered numbers isn't a number of season")
else:
    print(f'The season of entered months is: {season(_num_month)}')
