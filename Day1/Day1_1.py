import re

file = open("Day1.txt", "r")
lines = file.readlines()
file.close()

sum = 0
regex = re.compile(r"([+-])(\d+)")
for line in lines:
    erg = regex.match(line)
    num = int(erg.group(2))
    if erg.group(1) == "-":
        sum -= num
    else:
        sum += num
print(sum)