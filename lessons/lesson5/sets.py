# new_set = {2, 6, 4, 5, 0, True, False}
# print(new_set)
#
# set2 = {1, 1, 2, 2, 4, 4, 9}
# print(set2)
#
# empty_set = set()
# empty_dict = {}
# empty_dict2 = dict()
#
# name_set = {'sender', 'andrii', 'denis'}
# print(name_set)
#
# set3 = {5, 4, 3, 0.01}
# print(set3)
#
# # Addin 1 element
# set3.add('Name')
# set3.update(set2)
# print(set3)
# print(set2)
#
# new_dict = {
#     'name': 'den',
#     'age': 34,
#     'occupation': 'qa',
#
# }
#
# set3.update(new_dict)
# print(set3)
# set3.add("test")
# set3.union(name_set)
# print('union{}'.format(set3))
#
# set3.intersection_update(name_set)
# print(set3)
#
# set4 = set3.intersection(name_set)
# print('set4 {}'.format(set4))
# print('set3 {}'.format(set3))

_set1 = {1, 2, 3, 4, 5}
_set2 = {6, 7, 5, 4}
_set3 = _set1.difference(_set2)
print(_set3)

_set4 = _set2.difference(_set1)
print(_set4)

_set5 = _set1.symmetric_difference(_set2)
print(_set5)

_set2.difference_update(_set1)

print(_se2)