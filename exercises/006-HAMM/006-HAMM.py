with open("rosalind_hamm.txt", "r") as f:
    lines = f.readlines()

string1 = lines[0].strip()
string2 = lines[1].strip()

if len(string1) != len(string2):
    print "Length of strings differs!"
    quit()

hamm_distance = 0

for i in range(len(string1)):
    if string1[i] != string2[i]:
        hamm_distance += 1

print hamm_distance

