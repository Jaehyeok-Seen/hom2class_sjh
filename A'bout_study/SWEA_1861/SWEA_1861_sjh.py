import sys
sys.stdin = open('input.txt')

"""
현재 방 위치 = ?
이동할 수 있는 방의 수 = ?
제일 작은 수 부터 시작하면,이동할 수 있는 방의 개수가 최대인 방이 여럿이라면 그 중에서 적힌 수가 가장 작은 것을 출력한다.
이 조건 자동적으로 해결
출력은 이동해야할 위치 , 이동할 수 있는 방의 수
"""

def DFS(number): #방번호!
    global max_move
    x, y = information[number]
    move_cnt = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < N:
            if arr[nx][ny] == number+1: #방을 이동할 수 있는 조건
                x,y = nx,ny
                move_cnt = 1 + DFS(number+1)
                break
    return move_cnt

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    max_move = 0
    result_room = 0
    information = {}

    for i in range(N):
        for j in range(N):
            information[arr[i][j]] = (i,j)

    #모든 방에서 시작해보기
    for start in range(1,N*N+1):
        move_cnt = DFS(start)
        # 더 많이 이동할 수 있거나, 같은 횟수면 더 작은 방 번호
        if move_cnt > max_move:
            max_move = move_cnt
            result_room = start

    print(f'#{tc} {result_room} {max_move + 1}')  # 시작 방 포함
