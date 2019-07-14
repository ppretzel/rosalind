with open("rosalind_iev.txt", "r") as f:
    line = f.read()

couple_counts = map(int, line.strip().split())

expected_offspring = couple_counts[0] * 2 + \
                     couple_counts[1] * 2 + \
                     couple_counts[2] * 2 + \
                     couple_counts[3] * 2 * 0.75 + \
                     couple_counts[4] * 2 * 0.5 + \
                     couple_counts[5] * 2 * 0

print str(expected_offspring)
with open("result.txt", "w") as f:
    f.write(str(expected_offspring))
