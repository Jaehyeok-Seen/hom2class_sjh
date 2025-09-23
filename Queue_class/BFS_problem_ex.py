# =====================================================================
# 1. 미로 탈출 (최단경로)
# =====================================================================
from collections import deque


def maze_escape(maze):
    """
    미로에서 시작점(0,0)에서 도착점까지의 최단거리 찾기
    1: 벽, 0: 길
    """
    n = len(maze)
    m = len(maze[0])

    # 상하좌우 이동
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    while queue:
        x, y, dist = queue.popleft()

        # 도착점 도달
        if x == n - 1 and y == m - 1:
            return dist

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maze[nx][ny] == 0:
                    visited[nx][ny] = True
                    queue.append((nx, ny, dist + 1))

    return -1  # 경로 없음


# 테스트
maze = [
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
print(f"미로 최단거리: {maze_escape(maze)}")


# =====================================================================
# 2. 바이러스 확산 (시뮬레이션)
# =====================================================================
def virus_spread(grid, virus_positions):
    """
    바이러스가 모든 컴퓨터에 퍼지는 최소 시간 계산
    0: 빈공간, 1: 컴퓨터, 2: 감염된 컴퓨터
    """
    n = len(grid)
    m = len(grid[0])

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()

    # 초기 감염된 컴퓨터들을 큐에 추가
    for x, y in virus_positions:
        queue.append((x, y, 0))  # (x, y, 시간)
        grid[x][y] = 2

    max_time = 0

    while queue:
        x, y, time = queue.popleft()
        max_time = max(max_time, time)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] == 1:  # 아직 감염되지 않은 컴퓨터
                    grid[nx][ny] = 2  # 감염시킴
                    queue.append((nx, ny, time + 1))

    # 감염되지 않은 컴퓨터가 있는지 확인
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                return -1  # 모든 컴퓨터를 감염시킬 수 없음

    return max_time


# 테스트
grid = [
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1]
]
virus_pos = [(0, 0)]  # 초기 바이러스 위치
print(f"바이러스 확산 시간: {virus_spread(grid, virus_pos)}")


# =====================================================================
# 3. 섬의 개수 찾기
# =====================================================================
def count_islands(grid):
    """
    2D 그리드에서 섬의 개수 찾기
    1: 육지, 0: 물
    """
    if not grid:
        return 0

    n = len(grid)
    m = len(grid[0])
    visited = [[False] * m for _ in range(n)]
    islands = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y)])
        visited[start_x][start_y] = True

        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and grid[nx][ny] == 1:
                        visited[nx][ny] = True
                        queue.append((nx, ny))

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                bfs(i, j)  # 새로운 섬 발견시 BFS로 전체 탐색
                islands += 1

    return islands


# 테스트
island_grid = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1]
]
print(f"섬의 개수: {count_islands(island_grid)}")


# =====================================================================
# 4. 친구 관계 (그래프에서 최단거리)
# =====================================================================
def friend_distance(friends, person1, person2):
    """
    소셜 네트워크에서 두 사람 사이의 최단 친구 관계 거리
    """
    if person1 == person2:
        return 0

    queue = deque([(person1, 0)])  # (사람, 거리)
    visited = set([person1])

    while queue:
        current_person, distance = queue.popleft()

        # 현재 사람의 친구들 확인
        for friend in friends[current_person]:
            if friend == person2:
                return distance + 1

            if friend not in visited:
                visited.add(friend)
                queue.append((friend, distance + 1))

    return -1  # 연결되지 않음


# 테스트
friends_network = {
    'Alice': ['Bob', 'Charlie'],
    'Bob': ['Alice', 'David', 'Eve'],
    'Charlie': ['Alice', 'Frank'],
    'David': ['Bob'],
    'Eve': ['Bob', 'Frank'],
    'Frank': ['Charlie', 'Eve']
}
print(f"Alice와 Frank 사이 거리: {friend_distance(friends_network, 'Alice', 'Frank')}")


# =====================================================================
# 5. 게임 맵 최단거리 (프로그래머스 스타일)
# =====================================================================
def game_shortest_path(maps):
    """
    게임 맵에서 상대방 진영까지의 최단거리
    1: 갈 수 있는 곳, 0: 벽
    """
    n = len(maps)
    m = len(maps[0])

    # 목표지점 도달 불가능한 경우 미리 체크
    if maps[0][0] == 0 or maps[n - 1][m - 1] == 0:
        return -1

    queue = deque([(0, 0, 1)])  # (x, y, 거리)
    visited = [[False] * m for _ in range(n)]
    visited[0][0] = True

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        x, y, distance = queue.popleft()

        # 목표지점 도착
        if x == n - 1 and y == m - 1:
            return distance

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and maps[nx][ny] == 1:
                    visited[nx][ny] = True
                    queue.append((nx, ny, distance + 1))

    return -1


# 테스트
game_map = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]
print(f"게임 최단거리: {game_shortest_path(game_map)}")

# =====================================================================
# BFS의 핵심 활용 포인트
# =====================================================================
"""
BFS가 유용한 상황들:

1. 최단거리/최소시간 문제
   - 가중치가 없는 그래프에서 최단경로
   - 모든 간선의 비용이 1로 동일할 때

2. 레벨별 탐색
   - 시작점에서 거리별로 노드를 방문해야 할 때
   - 바이러스 확산, 물 채우기 등 시뮬레이션

3. 연결성 확인
   - 두 지점이 연결되어 있는지 확인
   - 섬의 개수, 연결 컴포넌트 찾기

4. 상태 공간 탐색
   - 게임 상태에서 목표 상태까지의 최소 이동
   - 퍼즐 문제 해결

핵심: BFS는 "너비 우선"이므로 가장 가까운 해답을 먼저 찾습니다!
"""