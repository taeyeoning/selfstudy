N, M = map(int, input().split())
mylist = [0]*N
temp = 0
for i in range(N) :
    mylist[i] = i + 1

for i in range(M) :
    a, b = map(int, input().split())
    temp = mylist[a-1]
    mylist[a-1] = mylist[b-1]
    mylist[b-1] = temp

for i in mylist :
    print(i, end = " ")