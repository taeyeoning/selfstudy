mylist = []

for i in range(30) :
    mylist.append(i + 1)

for i in range(28) :
    a = int(input())
    mylist.remove(a)

print(mylist[0])
print(mylist[1])