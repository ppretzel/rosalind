with open("rosalind_revc.txt", "r") as f:
    contents = f.read()

rev = reversed(contents.strip())

def complement(x):
    if x == "A":
        return "T"
    if x == "T":
        return "A"
    if x == "C":
        return "G"
    if x == "G":
        return "C"

rev_compl = map(complement, rev)

print rev_compl

with open("result.txt", "w") as f:
    f.write("".join(rev_compl))
