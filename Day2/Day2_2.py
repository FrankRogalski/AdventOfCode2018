file = open("Day2/Day2.txt", "r")
lines = file.readlines()
file.close()

diff = ""
def difference(line1, line2):
    global diff
    org = len(line1)

    line1 = list(line1)
    line2 = list(line2)
    
    if line1 == line2 or len(line1) != len(line2):
        return False

    for char in range(len(line1)):
        if line1[char] != line2[char]:
            line1[char] = ""
            line2[char] = ""

    line1 = "".join(line1)
    if org - len(line1) == 1:
        diff = line1
        return True

def main():
    for line in lines:
        for line2 in lines:
            if difference(line, line2):
                print(diff)

main()
