N, M = map(int, input().split()) # N * M 크기의 행렬
                                 # 가로가 N, 세로가 M
                                 # 그러면 2M 번 받아야됨

li = []

for _ in range(2 * M) : # 런타임 에러 해결 위함?
    numbers = list(map(int, input().split()))
    li.append(numbers)

for i in range(M) :
    for j in range(N) :
        print(li[i][j] + li[i + M][j], end = " ")
    print()