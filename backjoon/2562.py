mylist = []
k = 0
temp = 0

for i in range(9) :
    a = int(input())
    mylist.append(a)
    if a > k :
        k = a
        temp = i + 1

print(max(mylist))
print(temp)