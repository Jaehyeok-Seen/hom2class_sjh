# for i in range(1,4):
#     for j in range(1, 4):
#         print(i, j)




# def KFC(x):
#     if x == 4:
#         return
#     print(f'재귀전= {x}', end=" ")
#     KFC(x+1)
#     print(f'재귀= {x}', end=" ")
#
# x= 0
# KFC(0)
# print('끝')

# def SJH(n):
#     if n == 3:
#         return
#     print(f'전={n}',end=" ")
#     SJH(n+1)
#     SJH(n+1)
#     print(f'후={n}', end=" ")
#
# x = 0
# SJH(0)

# path = []
# def KFC(n):
#     if n ==3:
#         print(path)
#         return
#
#
#     for i in range(3):
#         path.append(i)
#         KFC(n+1)
#         path.pop()
# KFC(0)


# 1부터 6까지 사용하는 중복 순열 ( [1,1,1] ~ [6,6,6]) 을 출력하는 코드를 재귀호출로 구현
used = [False for _ in range(6)]
path =[]
def SJH(n):
    if n == 5:
        print(path)
        return

    for i in range(1,6):
        if used[i] == True:
            continue
        used[i] = True
        path.append(i)
        SJH(n+1)
        path.pop()
        used[i] = False

SJH(1)


used = [False] * 7
path = []
def quiz(n):
    if n == 6:
        print(path)
        return
    for i in range(1, 7):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        quiz(n+1)
        path.pop()

