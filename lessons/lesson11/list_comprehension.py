a = [1, 2, 3, 4, 5, 6, 7]


def get_sorted(_list):
    empty_list = []
    for i in _list:
        if i < 5:
            empty_list.append(i)
    print('Filtered list {}'.format(empty_list))


b = [x for x in a if x < 5]
get_sorted(a)

print(b)


message = input('Input: ')
vowels = ['a', 'A', 'e', 'E', 'o', 'O', 'i', 'I', 'u', 'U', 'y', 'Y']
print("output: {}".format(''.join(['' if ch in vowels else ch for ch in message])))

formated_message_list = ['' if ch in vowels else ch for ch in message]

joined_list = ', '.join(formated_message_list)
joined_list_a = ', '.join(str(a))

print(formated_message_list)
print(joined_list)

