with open("rosalind_fibd.txt", "r") as f:
    line = f.read()

(n, m) = map(int, line.strip().split())

population = [0 for i in range(m)]

#initialize first pair
population[0] = 1

# index i is month-1! 
for i in range(1,n):
    newborns = sum(population[1:len(population)])
    for j in range(m-1, 0, -1):
        population[j] = population[j-1]
    population[0] = newborns

    #print "Month {}: {}".format(i+1, sum(population))

print "Population after {} months: {}".format(n, sum(population))
with open("result.txt", "w") as f:
    f.write(str(sum(population)))
