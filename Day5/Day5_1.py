file = open("Day5/Day5.txt", "r")
lines = file.readlines()
file.close()

line = []
for chara in lines[0]:
    line.append(chara)

deleted = True
while deleted:
    deleted = False
    i = len(line) - 2
    while i >= 0:
        if line[i].upper() == line[i + 1].upper() and line[i] != line[i + 1]:
            deleted = True
            del line[i:i + 2]
            i -= 1
        i -= 1

print(len(line) - 1)
