N = int(input())
sol = []

for i in range(N) :
    how = int(input())
    q = 0
    d = 0
    n = 0
    p = 0
    while how // 25 > 0 :
        q += 1
        how -= 25
        
    while how // 10 > 0 :
        d += 1
        how -= 10
        
    while how // 5 > 0 :
        n += 1
        how -= 5
        
    while how // 1 > 0 :
        p += 1
        how -= 1
        
    sol.append([q, d, n, p])

for i in range(N) :
    for j in range (4) :
        print(sol[i][j], end = " ")
    print()