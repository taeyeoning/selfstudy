# C:/doit/game/__init__.py
from .graphic.render import render_test # 패키지 내의 다른 모듈을 미리 import해 간편하게 접근.

VERSION = 3.5

def print_version_info():
    print(f"The version of this game is {VERSION}.")

# 여기에 패키지 초기화 코드를 작성한다.
print("Initializing game ...")