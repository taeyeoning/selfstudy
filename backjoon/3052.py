b = [0] * 42
count = 0
for i in range(10) :
    a = input()
    a = int(a)
    k = a % 42
    b[k] = 1

for i in range(42) :
    if b[i] != 0 :
        count += 1

print(count) 