num = int(input())

a = []

for i in range(num) :
    b = list(map(int, input().split()))
    c = b[0] + b[1]
    a.append(c)

for i in range(num) :
    print(a[i])