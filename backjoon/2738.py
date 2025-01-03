## N, M 가로 세로 유의할 것!!!!

N, M = map(int, input().split())

li = []

for i in range(2 * N) :
    numbers = list(map(int, input().split()))
    li.append(numbers)

for i in range(N) :
    for j in range(M) :
        print(li[i][j] + li[i + N][j], end = " ")
    print()