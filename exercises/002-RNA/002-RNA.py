with open("rosalind_rna.txt", "r") as f:
    contents = f.read()

outdata = map(lambda x: "U" if x=="T" else x, contents)
print outdata

with open("002-RNA-result.txt", "w") as f:
    f.write("".join(outdata))
