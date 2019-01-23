import math

maxValue = 10000
threads = 4

summe = maxValue ** 2
used = 0
ant =  summe / threads
oldEnd = -1

for i in range(threads):
    start = oldEnd + 1
    end = math.sqrt(ant +  used)
    used += ant
    oldEnd = end