import re

def find_num(lines):
    sums = [0]
    sum = 0
    regex = re.compile(r"([+-])(\d+)")
    while True:
        for line in lines:
            erg = regex.match(line)
            num = int(erg.group(2))

            if erg.group(1) == "-":
                sum -= num
            else:
                sum += num

            if sum in sums:
                return sum
            sums.append(sum)


file = open("Day1.txt", "r")
lines_f = file.readlines()
file.close()
print(find_num(lines_f))
