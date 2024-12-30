N, M = input().split() # M 개 줄에 걸쳐서 바구니 N 개에 넣음
N = int(N)
M = int(M)
mylist = [0] * N

for i in range(M) :
    a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    for p in range(a, b+1) :
        mylist[p-1] = c

for i in mylist :
    print(i, end = " ")
###########
# a,b = map(int,input().split())
# nums = []
# for i in range(a):
#   nums.append(0)
# for i in range(b):
#   x,y,z = map(int, input().split())
#   for j in range(x-1,y):
#     nums[j] = z

# for i in nums:
#   print(i,end=' ')