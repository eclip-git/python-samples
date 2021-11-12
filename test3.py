users = {}
THRESHOLD = 0.4
MAX_SAMPLES = 5


def scorer(audio):
    for i in users:
        slist = users[i]['samples']
        for s in slist:
            score = predict(audio, s)
            if score > THRESHOLD:
                slist.append(audio)
                if len(slist) > MAX_SAMPLES:
                    slist.pop(1)
                users[i]['score'] = score
                return i

    uid = len(users)+1
    users[uid] = {'samples': [audio], 'score': 0.0}


def predict(a1, a2):
    if a1 == a2:
        return 1.0
    else:
        return 0.0


print(scorer("user1"))
print(scorer("user2"))
print(scorer("wow"))
print(scorer("user2"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))
print(scorer("wow"))




print(users)
