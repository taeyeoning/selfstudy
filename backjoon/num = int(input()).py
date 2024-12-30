num = int(input())

mylist = list(map(int, input().split()))

max = int(max(mylist))
min = int(min(mylist))

print(max * min)
