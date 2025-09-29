arr = ['A','B','C','D','E']
n = 3
# 5중에서 3개 선택해야하는 상황

path = []

def recur(cnt, start):
    if cnt == n:
        print(*path)
        return

    for i in range(start, len(arr)):
        path.append(arr[i])
        recur(cnt +1, i+1)
        path.pop()
recur(0,0)

path = []


