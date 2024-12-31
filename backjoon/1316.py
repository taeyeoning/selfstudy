N = int(input())
num = 0


for i in range(N) :
    char = input()
    li = [] # 알파벳 리스트를 만들어줄거임.
    kk = 0
    for i in char : # 단어 글자수만큼 
        if i not in li :
            li.append(i) # 처음보는 알파벳이면 li에 넣어줌
        elif i == li[-1] : # 있는데, 제일 마지막 문자랑 같음
                             # 그룹 문자일가능성 ㅇㅇ
            continue
        else : # 있는데 제일 마지막 문자랑 다름
            kk += 1
            break
    # 한  단어 다돌고나서
    if kk == 0 :
        num += 1

print(num)
