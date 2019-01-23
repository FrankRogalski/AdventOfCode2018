file = open("Day2/Day2.txt", "r")
lines = file.readlines()
file.close()

two_counter = 0
three_counter = 0

for line in lines:
    chars = {}
    for chara in line:
        chars[chara] = chars.get(chara, 0) + 1
    if 2 in chars.values():
        two_counter += 1
    if 3 in chars.values():
        three_counter += 1

print("{} twos * {} threes = {}".format(two_counter, three_counter, two_counter * three_counter))