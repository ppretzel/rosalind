with open("rosalind_fib.txt", "r") as f:
    contents = f.read()

n, k = contents.split()
n = int(n)
k = int(k)

second_last_month = 1
last_month = 1

for i in range(2, n):
    current_month = last_month + second_last_month * k
    second_last_month = last_month
    last_month = current_month

with open("result.txt", "w") as f:
    f.write(str(current_month))
    print current_month
