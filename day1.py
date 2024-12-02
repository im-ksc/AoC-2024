with open("input.txt") as f:
    left, right = [], []
    for line in f:
        line = line.split()
        left.append(int(line[0]))
        right.append(int(line[1]))

total_dist = sum(abs(right - left) for left, right in zip(sorted(left), sorted(right)))
similarity_score = sum(each * right.count(each) for each in left)

print(total_dist)
print(similarity_score)
