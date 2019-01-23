import re

file = open("Day3/Day3.txt", "r")
lines = file.readlines()
file.close()

maxx = 0
maxy = 0

regex = re.compile(r"\d+")

claims = []

for line in lines:
    values = regex.findall(line)

    for i in range(len(values)):
        values[i] = int(values[i])
    
    if (values[1] + values[3] > maxx):
        maxx = values[1] + values[3]

    if (values[2] + values[4] > maxy):
        maxy = values[2] + values[4]

    claims.append(values)

matrix = [[0 for x in range(maxx + 1)] for y in range(maxy + 1)]

for claim in claims:
    for x in range(claim[1], claim[1] + claim[3]):
        for y in range(claim[2], claim[2] + claim[4]):
            matrix[x][y] += 1

sum = 0

for x in range(len(matrix)):
    for y in range(len(matrix[0])):
        if (matrix[x][y] > 1):
            sum += 1

print(sum)