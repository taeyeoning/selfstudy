N,M = map(int, input().split())
mylist = []
temp = 0

for i in range(N) :
    mylist.append(i + 1)

for i in range(M) :
    j, k = map(int, input().split())
    while True :
        if j >= k : 
            break
        temp = mylist[j-1]
        mylist[j-1] = mylist[k-1]
        mylist[k-1] = temp
        j += 1
        k -= 1
        

for i in mylist :
    print(i, end = " ")