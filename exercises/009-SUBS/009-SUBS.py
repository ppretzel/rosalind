import re

with open("rosalind_subs.txt", "r") as f:
    lines = f.readlines()

string = lines[0].strip()
substring = lines[1].strip()

index_list = []

index = 0
while index < len(string):
    
    index = string.find(substring, index)
    if index == -1:
        break
    index += 1
    index_list.append(index)

res = " ".join(map(str,index_list))

print res
with open("result.txt", "w") as f:
    f.write(res)
