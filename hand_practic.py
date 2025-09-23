def __init__(self):
    self.data = []

def push(self,x):
    self.data.append(x)

def pop(self):
    if not self.data:
        return -1
    return self.data.pop()

def size(self):
    return len(self.data)

def empty(self):
    if not self.data:
        return 1
    return 0

def top(self):
    if not self.data:
        return -1
    return self.data[-1]

# 파이썬은 스택을 구현하기 위한 라이브러리가 따로 있다. 하지만, 기본 자료형인 리스만으로도 간단하게 스택을 다룰 수 있다.


stack = []  #빈 리스트 선언

for item in ["고기","빵","과일","채소"]:
    stack.append(item)

print(stack.pop())  #>>>채소 (가장 나중에 추가된 원소를 제거)

print(stack[-1])   # >>>과일

print("empty" if not stack else "not empty") #>>>not empty, 이렇게도 쓸 수 있구나

