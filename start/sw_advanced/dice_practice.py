"""
N개의 주사위를 던져 나올 수 있는 모든 중복 순열 (Type 1)과
순열 (Type 2)를 출력
숫자는 1~6까지
재귀는 2번만 호출
시작은 1

"""
path = []
used = [False] *7

def type1(current):
    if current ==2:
        print(path)
        return

    for i in range(1, 7):
        path.append(i)
        type1(current+1)
        path.pop()

type1(0)

path2 = []
used2 = [False]*7
def type2(current):
    if current ==2:
        print(path2)
        return

    for j in range(1,7):
        if used2[j]:
            continue
        path2.append(j)
        used2[j] = True
        type2(current+1)
        path2.pop()
        used2[j] = False

type2(0)