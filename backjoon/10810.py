N, M = input().split() # M 개 줄에 걸쳐서 바구니 N 개에 넣음
N = int(N)
M = int(M)
mylist = [0] * N

for i in range(len(mylist)-1) :
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    for p in range(a, b + 1) :
        mylist[p-1] = c

for i in range(len(mylist)) :
    print(mylist[i], end = " ")