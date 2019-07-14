import FASTAhelper

strings = FASTAhelper.readFASTA("rosalind_gc.txt")

def gc_percentage(string):

    gc_count = len(filter(lambda x: x == "G" or x == "C", string))
    gc_percentage = float(gc_count) / len(string) * 100
    return gc_percentage

gc_percentages = {k: gc_percentage(v) for (k, v) in strings.items()}

# key of the string with the maximum gc percentage
max_key = max(gc_percentages, key=gc_percentages.get)

# result string
res = max_key + "\n" + str(gc_percentages[max_key])

print res
with open("result.txt", "w") as f:
    f.write(res)
