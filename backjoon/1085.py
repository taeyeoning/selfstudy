x, y, w, h = map(int,input().split())

newx = min(abs(x), abs(x - w),abs(h-y), abs(y))

print(newx)