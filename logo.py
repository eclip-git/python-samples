def logo(s):
    occur = {}
    for i in s:
        if i in occur:
            occur[i] = occur[i]+1
        else:
            occur[i] = 1

    sorted_occur = sorted(occur, key=occur.get, reverse=True)

    for i in sorted_occur[:3]:
        print(i, occur[i])


def logo2(s):
    occur = {}

    for c in sorted(s):
        occur[c] = occur.get(c, 0) + 1

    letters = sorted(occur, key=occur.get, reverse=True)

    for k in letters[:3]:
        print(k, occur[k])


logo("google")
logo2("google")
