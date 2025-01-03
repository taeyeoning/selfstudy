n = int(input())
li = [[0 for _ in range(100)] for _ in range(100)]

for i in range(n) : # 반복횟수
    g, s = map(int, input().split())
    for j in range(g, min(100, g + 10)) : # 가로
        for k in range(s, min(100, s + 10)) : # 세로
            li[j][k] = 1
            
a = 0

for row in li :
    a += sum(row)

print(a)