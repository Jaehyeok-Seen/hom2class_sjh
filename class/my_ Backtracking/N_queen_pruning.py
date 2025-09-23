#기울기를 생각해서 1, -1일 때 대각의 지나오 지점들을 다 구해올 수 있다.
if abs(row-preve_row) == abs(visited(row) - visited[prev_row]):
    return False

    for col in range(N):
        visited[row] = col #현재 row의 col에 놓았다라고 가정하고
        if not check(row):