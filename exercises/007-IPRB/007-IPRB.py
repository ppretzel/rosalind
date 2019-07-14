with open("rosalind_iprb.txt", "r") as f:
    line = f.read()

(k, m, n) = map(float, line.split())

t = float(k+m+n)

res = k/t + \
        m/t*k/(t-1) + m/t*(m-1)/(t-1)*0.75 + m/t * n/(t-1)*0.5 + \
        n/t * k/(t-1) + n/t*m/(t-1)*0.5

print res
with open("result.txt", "w") as f:
    f.write(str(res))
