a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
e = list(map(int, input().split()))
f = list(map(int, input().split()))
g = list(map(int, input().split()))
h = list(map(int, input().split()))
i = list(map(int, input().split()))

li = a + b + c + d + e + f + g + h + i
maxi = max(li)
li= []
li.append(a)
li.append(b)
li.append(c)
li.append(d)
li.append(e)
li.append(f)
li.append(g)
li.append(h)
li.append(i)

n = 1
m = 1
print(maxi)
for i in range(9) :
    for j in range(9) :
        if li[i][j] == maxi :
           n = i + 1
           m = j + 1
           break

print(n, m)