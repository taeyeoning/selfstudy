def add(a,b):
    return a + b

def sub(a, b):
    return a - b

# print(add(1,4)) # 얘네가 그냥 이렇게 있으면, 다른 데에서 import할 때 바로 실행되어버림.
# print(sub(4,2))

if __name__ == "__main__": # 직접 이 mod1 파일을 실행할 경우, __name__ 변수에는 __main__ 값이 저장된다.
                           # 다른 파이썬 모듈에서 mod1 을 import할 경우, __name__ 변수에는 모듈 이름인 mod1 이 저장된다.
    print(add(1,4)) # 직접 이 파일을 실행했을 경우에만 출력됨. 다른 파일에서 import된 경우에는 pass.
    print(sub(4,2))