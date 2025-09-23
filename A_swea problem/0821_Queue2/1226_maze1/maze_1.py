import sys
sys.stdin = open('input (1).txt')

from collections import deque

"""
테스트 케이스에서
0 : 길
1 : 벽
2 : 출발점
3 : 도착점
도달 가능 여부를 1 or 0으로 표시(1 = 가능, 0 = 불가능)
"""
def validation_maze(maze_arr):
    #출발점이 고정 (1,1)
    queue = deque([(1,1)])
    visited = [[0]*16 for _ in range(16)]
    visited[1][1] = True

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    while queue: #queue가 비어있지 않다면 무한 반복
        x,y = queue.popleft()
        if maze_arr[x][y] == '3': #큐에서 꺼냈을때 좌표값이 3이면 골인한거니까 그 즉시 종료
            return 1  #반환해야하는 1을 리턴

        for i in range(4):
            nx = x + di[i]
            ny = y + dj[i]
        #방향탐색을 해서
            if 0<= nx < 16 and 0<= ny < 16:
                #벽을 벗어나지 않고
                if not visited[nx][ny] and maze_arr[nx][ny] != '1':  #벽인 1이 아니라면 방향탐색한 값을
                    visited[nx][ny] = True
                    queue.append((nx,ny))    #큐에 담는다.

    return 0

T = 10
for i in range(1,T+1):
    tc = int(input())
    maze_arr = ["".join(input()) for _ in range(16)]

    result = validation_maze(maze_arr)
    print(f'#{tc} {result}')
