list1 = ['a', 'b', 'c']
dict1 = {'a': 3, 'b': 1, 'c': 2}

print(list1)

print(sorted(list1, reverse=True))
print(list1[::-1])
print(dict1)
print(sorted(dict1))
print(sorted(dict1, key=dict1.get, reverse=True))
# print(sorted(dict1, key=dict1.pop, reverse=True))
print(dict1)
print(dict1.pop('b'))
print(dict1)