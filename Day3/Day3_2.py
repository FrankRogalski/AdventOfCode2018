import re

file = open("Day3/Day3.txt", "r")
lines = file.readlines()
file.close()

regex = re.compile(r"\d+")

claims = []

for line in lines:
    values = regex.findall(line)

    for i in range(len(values)):
        values[i] = int(values[i])

    claims.append(values)

def overlaps(claim1, claim2):
    if claim1[1] + claim1[3] > claim2[1] \
        and claim1[1] < claim2[1] + claim2[3] \
        and claim1[2] + claim1[4] > claim2[2] \
        and claim1[2] < claim2[2] + claim2[4]:
        return True
    return False

for claim1 in claims:
    overlap = False

    for claim2 in claims:
        if claim1[0] != claim2[0] and overlaps(claim1, claim2):
            overlap = True
            break

    if not overlap:
        print(claim1[0])
    