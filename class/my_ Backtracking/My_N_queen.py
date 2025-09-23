def recur(row):
    global answer

    if row == N:
        answer += 1
        return

    for col in range(N):
        if not check(row,col):
            continue

        visited[row][col] = 1
        path.append(col)
        recur(row + 1)
        path.pop()
        visited[row][col] = 0


def check(row, col):
    # 3가지 경우
    # 가로 행에 들린적이 있는지
    for i in range(row):
        if visited[i][col]:
            return False
    # \
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if visited[i][j]:
            return False
        i -= 1
        j -= 1

    # /
    i, j = row - 1, col + 1
    while i >= 0 and j < N:
        if visited[i][j]:
            return False
        i -= 1
        j += 1

    return True

N= 4
answer = 0
path = []
visited = [[0] * N for _ in range(N)]

recur(0)
print(answer)

