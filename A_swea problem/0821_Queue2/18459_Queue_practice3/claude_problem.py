from collections import deque


def bfs_graph(graph, start):
    """
    그래프에서 BFS를 수행하는 함수

    Args:
        graph: 인접 리스트로 표현된 그래프 (딕셔너리)
        start: 시작 노드

    Returns:
        visited_order: 방문한 노드들의 순서 (리스트)
    """
    visited = set()  # 방문한 노드들을 저장
    queue = deque([start])  # BFS를 위한 큐
    visited_order = []  # 방문 순서를 기록

    visited.add(start)

    while queue:
        node = queue.popleft()  # 큐에서 노드를 꺼냄
        visited_order.append(node)

        # 현재 노드의 모든 인접 노드를 확인
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visited_order


def bfs_shortest_path(graph, start, end):
    """
    BFS를 사용하여 두 노드 간의 최단 경로를 찾는 함수

    Args:
        graph: 인접 리스트로 표현된 그래프
        start: 시작 노드
        end: 목표 노드

    Returns:
        path: 최단 경로 (리스트), 경로가 없으면 None
    """
    if start == end:
        return [start]

    visited = set()
    queue = deque([(start, [start])])  # (현재 노드, 경로)
    visited.add(start)

    while queue:
        node, path = queue.popleft()

        for neighbor in graph.get(node, []):
            if neighbor == end:
                return path + [neighbor]

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None  # 경로가 없음


def bfs_matrix(matrix, start_row, start_col):
    """
    2D 매트릭스에서 BFS를 수행하는 함수 (미로, 격자 등에 사용)

    Args:
        matrix: 2D 리스트 (0: 갈 수 있는 곳, 1: 벽)
        start_row: 시작 행
        start_col: 시작 열

    Returns:
        visited_cells: 방문한 셀들의 좌표 리스트
    """
    if not matrix or not matrix[0]:
        return []

    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    queue = deque([(start_row, start_col)])
    visited_cells = []

    # 상하좌우 방향
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    visited.add((start_row, start_col))

    while queue:
        row, col = queue.popleft()
        visited_cells.append((row, col))

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            # 경계 확인 및 방문 여부, 벽 여부 확인
            if (0 <= new_row < rows and 0 <= new_col < cols and
                    (new_row, new_col) not in visited and
                    matrix[new_row][new_col] == 0):
                visited.add((new_row, new_col))
                queue.append((new_row, new_col))

    return visited_cells


# 사용 예제
if __name__ == "__main__":
    # 예제 1: 그래프 BFS
    print("=== 그래프 BFS 예제 ===")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    result = bfs_graph(graph, 'A')
    print(f"시작점 A에서 BFS 탐색 순서: {result}")

    # 예제 2: 최단 경로 찾기
    print("\n=== 최단 경로 찾기 예제 ===")
    path = bfs_shortest_path(graph, 'A', 'F')
    print(f"A에서 F까지의 최단 경로: {path}")

    # 예제 3: 2D 매트릭스 BFS
    print("\n=== 2D 매트릭스 BFS 예제 ===")
    matrix = [
        [0, 0, 1, 0],
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0]
    ]

    visited_cells = bfs_matrix(matrix, 0, 0)
    print(f"(0,0)에서 시작한 BFS 방문 순서: {visited_cells}")

    # 매트릭스 시각화
    print("\n매트릭스 (0: 갈 수 있는 곳, 1: 벽):")
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if (i, j) in visited_cells:
                print(f"V", end=" ")  # 방문한 곳
            elif cell == 1:
                print("■", end=" ")  # 벽
            else:
                print("□", end=" ")  # 갈 수 없는 곳
        print()