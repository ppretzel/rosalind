from FASTAhelper import readFASTA

dna_strings = readFASTA("rosalind_cons.txt")

def base_to_row(base):
    if base == "A": return 0
    if base == "C": return 1
    if base == "G": return 2
    if base == "T": return 3
    return None

def row_to_base(row):
    if row == 0: return "A"
    if row == 1: return "C"
    if row == 2: return "G"
    if row == 3: return "T"
    return None

def max_base_at_position(i):
    max_val = max(profile_matrix[0][i],
                  profile_matrix[1][i],
                  profile_matrix[2][i],
                  profile_matrix[3][i])
    for j in range(4):
        if profile_matrix[j][i] == max_val:
            return row_to_base(j)

height = 4
width = len(dna_strings.values()[0])

profile_matrix = [[0 for i in range(width)] for j in range(height)]

for string in dna_strings.values():
    for i in range(len(string)):
        profile_matrix[base_to_row(string[i])][i] += 1

cons_string = ""
for i in range(width):
    cons_string += max_base_at_position(i)

print cons_string
print profile_matrix
with open("result.txt", "w") as f:
    f.write(cons_string + "\n")
    for i in range(4): 
        f.write(row_to_base(i) + ": ")
        f.write(" ".join(map(str, profile_matrix[i])) + "\n")
