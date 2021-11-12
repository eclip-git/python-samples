def ispal(s):
    s1 = s.lower()
    s2 = ""
    for i in range(len(s)-1, -1, -1):
        s2 += s1[i]

    return s1 == s2


def ispal2(s):
    s1 = s.lower()
    s2 = s1[::-1]

    return s1 == s2


print(ispal("babab"))
print(ispal2("babab"))
