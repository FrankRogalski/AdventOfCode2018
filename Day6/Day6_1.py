import re
import sys

def get_points():
    file = open("Day6/Day6.txt", "r")
    lines = file.readlines()
    file.close()

    points = []
    regex = re.compile(r"\d+")
    i = 0
    for line in lines:
        point = {}
        point["values"] = regex.findall(line)
        for j in range(len(point["values"])):
            point["values"][j] = int(point["values"][j])
        point["key"] = str(i)
        points.append(point)
        i += 1
    return points

def get_avg(points):
    durch_x = 0
    durch_y = 0
    for point in points:
        durch_x += point["values"][0]
        durch_y += point["values"][1]

    durch_x /= len(points)
    durch_y /= len(points)
    return int(durch_x), int(durch_y)

def calc_dist(auto_point, own_point):
    return abs(auto_point[0] - own_point[0]) + abs(auto_point[1] - own_point[1])

def calc_nearest_points(own_point, points):
    mini = sys.maxsize
    point_name = ""
    for point in points:
        dist = calc_dist(point["values"], own_point)
        if dist < mini:
            mini = dist
            point_name = point["key"]
        elif dist == mini:
            return "."
    return point_name

def calc_points(points, x, y, max_start, max_end):
    point_values = {}
    maxi = max_start
    i = 0
    touched_points = {}
    while True:
        
        for k in range(-maxi, maxi):
            key = "."
            point = ()
            if i == 0:
                point = (k + x, -maxi + y)
            elif i == 1:
                point = (maxi + x, k + y)
            elif i == 2:
                point = (k + x, maxi + y)
            elif i == 3:
                point = (-maxi + x, k + y)

            key = calc_nearest_points(point, points)
            point_values[key] = point_values.get(key, 0) + 1
            touched_points[key] = touched_points.get(key, 0) + 1

        i += 1
        if i % 4 == 0:
            if maxi % 100 == 0:
                print(maxi)
            if maxi >= max_end:
                
                keys = tuple(point_values.keys())
                for key in keys:
                    if key == "." or key in touched_points:
                        del point_values[key]
                break
            
            maxi += 1
            touched_points = {}
            i = 0
    return max(point_values.values())

def main():
    points = get_points()
    x, y = get_avg(points)
    print(calc_points(points, x, y, 0, 100))
    
main()