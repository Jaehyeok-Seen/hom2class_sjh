from collections import deque

def maze_escape(maze):
    """
    미로에서 시작점(0,0) 에서 도착점까지의 최단거리 찾기
    1: 벽, 0: 길

    """
    n = len(maze)
    m = len(maze[0])

    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    queue = deque([(0,0,1)]) #큐에 0,0시작점과 거리를 담는다.
    visited = [[False]*m for _ in range(n)]
    visited[0][0] = True #시작점은 방문했으니까?

    while queue: #큐가 비어있지 않다면
        x, y, dist = queue.popleft()

        # 도착점에 도달할 경우
        if x == n-1 and y == m-1:  # n x m 행렬에서 도착점은 [n-1][m-1]
            return dist

        for i in range(4): #(상하좌우)
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] == 0: #방문한적이 없고,벽이 아닌 길에 있다면
                    visited[nx][ny] = True
                    queue.append((nx,ny,dist+1))

    return -1 #경로 없음

# 테스트
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
print(f"미로 최단거리: {maze_escape(maze)}")