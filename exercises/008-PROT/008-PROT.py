from protein import rna_to_protein

with open("rosalind_prot.txt", "r") as f:
    line = f.read()

rna_string = line.strip()

# split in triplets
triplets = [rna_string[i:i+3] for i in range(0, len(rna_string), 3)]

# translate to proteins
proteins = map(rna_to_protein, triplets)

# remove stop sequence
proteins = filter(lambda x: x != "Stop", proteins)

res = "".join(proteins)
print res
with open("result.txt", "w") as f:
    f.write(res)
