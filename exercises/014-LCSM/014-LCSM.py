from FASTAhelper import readFASTA

strings = readFASTA("rosalind_lcsm.txt")

# find shortest string and generate possible substrings from this one, 
# since the longest shared motif can't be longer than the shortest string
string_lengths = {k: len(v) for k, v in strings.items()}
shortest_string_key = min(string_lengths, key = string_lengths.get)

# build a generator that yields substrings, starting with the longest ones,
# since we're looking for the longest common substring
def substring_generator(string):
    string_length = len(string)
    for i in range(1, string_length):
        for j in range(i+1):
            yield string[j:string_length-i+j]

substrings = substring_generator(strings[shortest_string_key])

# check these substrings against all other strings until the longest shared motif is found
# problem here: if a substring appears twice, it will be searched twice
for substring in substrings:
    found_lsm = True
    for key, string in strings.items():
        if string.find(substring) < 0:
            # as soon as the current substring isn't a substring of a string
            # it can't be the shared motif, therefore we can skip to the next substring
            found_lsm = False
            break
    if found_lsm:
       # once execution reaches this code, the current substring has been found in all strings
       # and therefore is the longest shared motif
       longest_shared_motif = substring
       break

# wrap it up
print "longest shared motif: " + longest_shared_motif
with open("result.txt", "w") as f:
    f.write(longest_shared_motif)
