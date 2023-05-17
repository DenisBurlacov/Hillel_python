# Тернарний if - 2 приклади.
# В данном варианте вписла 2 тернарных оператора в блок  if elif

bonus_card_lever = int(input('Please enter your bonus card level '))
if bonus_card_lever != 0 and bonus_card_lever < 100:
    bonus = 10 if bonus_card_lever >= 50 else 5
    print(f'Your current discount is {bonus}%')
elif bonus_card_lever >= 100:
    bonus = 80 if bonus_card_lever <= 1000 else 100
    print(f'Your current discount is {bonus}%')
else:
    print("Your current bonus not enough fo discount")


