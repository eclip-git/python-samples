import collections

a0 = [9, 3, 5, 9, 10]
a1 = [2, 5, 8, 10, 11, 12, 9]
a3 = [3, 3, 3, 3, 3]
s4 = {1, 3, 5, 2, 1}

a0_1 = list(dict.fromkeys(a0))

a2 = a0_1+[i for i in a1 if i not in a0_1]
a2.sort()

d = dict.fromkeys(a0)
print(d)
sorted_dict = collections.OrderedDict(d)
print(sorted_dict)
s = set(a0)
print(set(a3))

print(d)
print(s)
print(s4)

print(a0_1)
print(a2)



