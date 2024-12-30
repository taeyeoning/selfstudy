X = int(input())
N = int(input())
total = 0
b = 0
c = []

for i in range(N) :
    c.append(list(map(int, input().split())))

for i in range(N) :
    total += c[i][0] * c[i][1]

if X == total :
    print("Yes")
else :
    print("No")