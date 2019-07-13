f = open("rosalind_dna.txt", "r")

content = f.read()

def count(character, content):
    return len(filter(lambda char: char == character, content))

a = count("A", content)
t = count("T", content)
c = count("C", content)
g = count("G", content)

print "%s %s %s %s" % (a, c, g, t)
