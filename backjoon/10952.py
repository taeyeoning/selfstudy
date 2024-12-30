# A = 1
# B = 1
# i = 0
# mylist = []
# sol = []

# while (A != 0 & B != 0) :
#     mylist.append(list(map(int, input().split())))
#     A = mylist[i][0]
#     B = mylist[i][1]
#     sol.append(A + B)

# for i in range(len(mylist)) :
#     print(sol[i])

while True :
    A, B = input().split()
    A = int(A)
    B = int(B)
    if A == 0 & B == 0 :
        break
    print(A + B)


    