# 원본
# 경로 탐색 알고리즘
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if (nr, nc) == target:
                return actions + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != wall and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []


# 수정본
# 경로 탐색 알고리즘
def bfs(grid, start, target, wall):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        (r, c), actions = queue.popleft()

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc
            if (nr, nc) == target:
                return actions + [FIRE_CMDS[d]]

        for d, (dr, dc) in enumerate(DIRS):
            nr, nc = r + dr, c + dc

            # 수정: W(물)도 벽과 동일하게 취급하도록 조건 추가
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] not in (wall, 'W') and (nr, nc) not in visited:  # <-- 수정
                visited.add((nr, nc))
                queue.append(((nr, nc), actions + [MOVE_CMDS[d]]))

    return []