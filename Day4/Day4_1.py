import re

def read_file(path):
    file = open(path, "r")
    lines = file.readlines()
    file.close()
    return lines

def get_guard_lines(lines):
    guard_lines = []
    regex_general = re.compile(r"\[(\d+)\-(\d+)\-(\d+) (\d+):(\d+)\] (.*)")
    regex_end = re.compile(r"#(\d+)")
    for line in lines:
        general = regex_general.match(line)
        code = ""
        end = regex_end.search(general.group(6))

        if end:
            code = end.group(1)
        elif general.group(6)[0] == "f":
            code = "f"
        else:
            code = "w"

        guard_lines.append([general.group(1), general.group(2), general.group(3), general.group(4), general.group(5), code])
    return guard_lines

def get_guards(guard_lines):
    guards = {}
    guard_key = ""
    for guard_line in guard_lines:
        if guard_line[5] != "f" and guard_line[5] != "w":
            guard_key = guard_line[5]
            guards[guard_key] = guards.get(guard_key, {"lines": []})
            guards[guard_key]["key"] = guard_key
        else:
            guards[guard_key]["lines"].append(guard_line)

    return guards.values()

def count_minutes(guards):
    for guard in guards:
        guard["min"] = [0 for i in range(60)]
        prev_time = 0
        
        for line in guard["lines"]:
            if line[5] == "w":
                for i in range(prev_time, int(line[4])):
                    guard["min"][i] += 1
            prev_time = int(line[4])

def add_minutes(guards):
    for guard in guards:
        guard["total"] = 0
        for minu in guard["min"]:
            guard["total"] += minu

lines = read_file("Day4/Day4.txt")
guard_lines = get_guard_lines(lines)
guard_lines.sort(key=lambda table: "".join(table[:5]))
guards = get_guards(guard_lines)
count_minutes(guards)
add_minutes(guards)

max_guard = max(guards, key=lambda guard: guard["total"])
max_min = max(max_guard["min"])
max_min = max_guard["min"].index(max_min)
mult = int(max_guard["key"]) * max_min
print("{} Minuten * GuardID {} = {}".format(max_min, max_guard["key"], mult))