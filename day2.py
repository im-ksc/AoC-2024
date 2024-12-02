def safe(level):
    check_inc_decr = level[1] - level[0]
    for i in range(1, len(level)):
        x = level[i] - level[i-1]
        if abs(x) not in range(1, 4):
            return False
        if (check_inc_decr < 0 and x > 0) or (check_inc_decr > 0 and x < 0):
            return False
    return True

def problem_dampener(level):
    for i in range(len(level)):
        level_removed = level[:]
        level_removed.pop(i)
        if safe(level_removed):
            return True
    return False

def main():
    with open("input.txt") as f:
        safe1, safe2 = 0, 0
        for line in f:
            level = [int(level) for level in line.split()]
            if safe(level):
                safe1 += 1
                safe2 += 1
                continue
            if problem_dampener(level):
                safe2 += 1
    return safe1, safe2

safe1, safe2 = main()
print(safe1, safe2)
