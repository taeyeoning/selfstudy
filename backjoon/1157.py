word = input().upper()
freq = {}

# 딕셔너리
for i in word :
    if i in freq :
        freq[i] += 1
    else :
        freq[i] = 1

max_freq = max(freq.values())
most_common = [key for key, value in freq.items()
               if value == max_freq]

if len(most_common) >= 2 :
    print("?")
else : print(most_common[0])