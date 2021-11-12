def merge(s, k):

    for i in range(0, len(s), k):
        s1 = s[i:i+k]
        l1 = ''.join(set(s1))
        print(l1)


merge("teeoff", 3)

