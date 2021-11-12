list1 = [1, 2, 5, 9]
list2 = [3, 5, 9, 10]


def merge(l1, l2):
    l3 = l1
    for i in l2:
        if i not in l1:
            l3.append(i)
    return l3


lm = merge(list1, list2)
print(lm)
