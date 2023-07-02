# 1. Створити файл та записати в нього рядок.
with open('my_task.txt', 'w') as f:
    f.write('Some text, for the file write')

# 2.Прочитати створений файл та вивести на консоль вміст файлу
text_file = open('my_task.txt', 'r')
file_content = text_file.read()
print(file_content)
text_file.close()


# 3.Додати ще один рядок до створеного файлу.
with open('my_task.txt', 'a') as f:
    f.write('\nSome additional row to the file')



# 4.Прочитати всі рядки з файлу та вивести на консоль.
text_file = open('my_task.txt', 'r')
text = text_file.readlines()
for i in text:
    print(i.strip())
text_file.close()

# 5.* Записати у файл все що користувач введе з консолі. (Якщо хочете більш ніж один рядок спробуйте використати
# while True і перевірку на введений рядок, типу якщо exit тоді це кінець.)

with open('user_input_file.txt', 'w') as f:
    while True:
        input_text = input('Please enter some text, or "exit" to finish: ')
        if input_text.lower() == 'exit':
            break
        f.write(input_text + '\n')

text_file = open('user_input_file.txt', 'r')
file_content = text_file.read()
print(file_content)
text_file.close()