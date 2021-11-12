gbo = {'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'}

# {'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}.

owners = {}

for key, value in gbo.items():
    if value not in owners:
        owners[value] = [key]
    else:
        owners[value].append(key)

print(owners)
