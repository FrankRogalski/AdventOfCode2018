file = open("Day5/Day5.txt", "r")
lines = file.readlines()
file.close()

def removed_list(liste, char):
    new_list = []
    for l in liste:
        if l.upper() != char.upper():
            new_list.append(l)
    return new_list

line = []
for chara in lines[0]:
    line.append(chara)

results = []
for chara in "abcdefghijklmnopqrstuvwxyz":
    loop_line = removed_list(line, chara)
    deleted = True
    while deleted:
        deleted = False
        i = len(loop_line) - 2
        while i >= 0:
            if loop_line[i].upper() == loop_line[i + 1].upper() and loop_line[i] != loop_line[i + 1]:
                deleted = True
                del loop_line[i:i + 2]
                i -= 1
            i -= 1
    results.append({"key": chara, "chars": len(loop_line)})
    print(chara)

best_result = min(results, key=lambda result: result["chars"])
print(best_result["chars"])
