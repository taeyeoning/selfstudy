T = int(input())
c = []
d = []
a = 0

for i in range(T) :
    c.append(list(map(int, input().split())))

for i in range(T) :
    a = c[i][0] + c[i][1]
    d.append(a)

for i in range(T) :
    print("Case #%d:" % (i + 1),c[i][0], "+", c[i][1], "=", d[i])