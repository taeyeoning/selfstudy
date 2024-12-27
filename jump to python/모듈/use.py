import mod1
print(mod1.add(3,4))
print(mod1.sub(4,2))

from mod1 import add, sub # 모듈 이름을 붙이지 않고, 바로 해당 모듈의 함수를 쓸 수 있음
print(add(3,4))
print(sub(3,4))


from mod1 import * # 모든 함수를 불러와 사용하겠다는 의미