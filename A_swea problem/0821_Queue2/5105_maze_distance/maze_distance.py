import sys
sys.stdin = open('5105_input.txt')

from _collections import deque

"""
NxN 크기의 미로 
이때 최소 몇개의 칸을 지나야 출발지에서 도착지에 다다를 수 있는지 출력
경로가 있는 경우 최소한의 칸수를 출력, 경로가 없는 경우 0을 출력한다.
벽 : 1
통로 : 0

"""

def maze_explore(arr):

    # 출발지는 2인값의 좌표
    start_x, start_y = None, None    # ""로 했었는데 None으로 하면되는거였음
    goal_x, goal_y = None, None
    # 도착지는 3인값의 좌표
    for i in range(N):
        for j in range(N):

            if arr[i][j] == '2':  # 처음에 int로 비교하는 실수했었음
                start_x , start_y = i, j

            elif arr[i][j] == '3':
                goal_x , goal_y = i, j
    distance = 0

    if start_x is None or goal_x is None:
        return 0
    #확인용
    # print(f'시작점 : ({start_x},{start_y})')
    # print(f'도착점 : ({goal_x},{goal_y})')

    queue = deque([(start_x,start_y,0)]) #큐를 만들어서 시작점을 넣어두기,
    # ([start_x,start_y,0])이 되면 개별 숫자들이 들어가면서 타입 에러 발생

    visited = [[False]*N for _ in range(N)]
    visited[start_x][start_y] = True

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    while queue: #큐가 비어있지 않다면
        x, y ,distance = queue.popleft()
        if x == goal_x and y == goal_y: #도착점에 도달한거라면
            return distance-1 #도착하면서도 +1하게 되는거라

        for i  in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N: # 범위를 초과하지 않을 때
                if not visited[nx][ny] and arr[nx][ny] != '1': # 방문한 적이 없거나 벽(1)이 아닌경우
                    visited[nx][ny] = True # 방문한걸로 바꾸고
                    queue.append((nx , ny, distance + 1))  # 큐에 좌표와 거리를 +1해서 담는다


    return 0





T = int(input())

for tc in range(1,T+1):
    N = int(input())
    maze_arr = [list("".join(input())) for _ in range(N)]

    result = maze_explore(maze_arr)

    print(f'#{tc} {result}')