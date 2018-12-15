l = [1, 2, 3, 4, 5]
lsum = dif = sum(l)
rsum = 0
for i in l:
    rsum += i
    lsum -= i
    print(rsum,lsum)
    if abs(lsum - rsum) < dif:
        dif = abs(lsum - rsum)
        print(dif)
print(dif)
