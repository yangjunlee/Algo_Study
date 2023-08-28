from math import factorial
m = int (input())
site=[]
for _ in range(m):
    site.append(list(map(int, input().split())))
for a in site:
    a.sort()
    print(factorial(a[1])//factorial(a[0])//factorial(a[1]-a[0]))
