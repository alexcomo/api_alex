# n=int(input())
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
#
# print (d)
#

d = {'a': 1,'b': 2,'c': 3}
k = ' '
v = 0
for key, val in d:
    if v < val:
        k, v = key, val

print()