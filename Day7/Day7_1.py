import re

file = open("Day7/Day7.txt", "r")
lines = file.readlines()
file.close()

def remove_adjacent(seq):
    i = 1
    n = len(seq)
    while i < n:
        if seq[i] == seq[i-1]:
            del seq[i]
            n -= 1
        else:
            i += 1

regex = re.compile(r" ([A-Z]) ")
keys = {}
for line in lines:
    ergs = regex.findall(line)
    erg = keys.get(ergs[1], -1)
    if erg != -1:
        keys[ergs[1]].append(ergs[0])
    else:
        keys[ergs[1]] = [ergs[0]]
    
    erg = keys.get(ergs[0], -1)
    if erg == -1:
        keys[ergs[0]] = []

result = ""
deletables = []
while len(keys) > 0:
    for key, befores in keys.items():
        if len(befores) == 0:
            deletables.append(key)

    deletables.sort()
    remove_adjacent(deletables)
    for key, befores in keys.items():
        if deletables[0] in befores:
            keys[key].remove(deletables[0])
            
    del keys[deletables[0]]
    result += deletables[0]
    del deletables[0]

print(result)