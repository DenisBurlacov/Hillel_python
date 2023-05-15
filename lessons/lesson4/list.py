import copy
old_list = []
print(id(old_list))

new_list = list()
print(id(new_list))

copy_list = new_list
print(id(copy_list))

if id(new_list) == id(copy_list):
    print("the lists identical")

shallow_list = new_list.copy()

copy_list.append(1)

new_list = list()
print(id(new_list))

copy_list = new_list
print(id(copy_list))

if id(new_list) == id(copy_list):
    print("the lists identical")

original_nested_list = [1, 2, 3, [9, 1, 2], 4]
print(id(original_nested_list))
link_copy = original_nested_list
print(id(link_copy))

link_copy1 = original_nested_list.copy()
print(id(link_copy1))

print("\n\n")
print('_' * 15)

