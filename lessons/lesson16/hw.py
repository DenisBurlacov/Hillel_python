lines = []
while True:
    line = input('> ')
    if line == 'exit':
        break
    lines.append(line + '\n')

with open("some_text.txt", 'w') as f:
    f.writelines(lines)
