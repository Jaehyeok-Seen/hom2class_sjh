import sys

sys.stdin = open('sample_input.txt')
from heapq import heappush, heappop


def dijkstra():
    pq = []
    heappush(pq, (0, 0, 0))  # (연료, x, y)
    min_fuel_to = [[float('inf')] * N for _ in range(N)]
    min_fuel_to[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        fuel, x, y = heappop(pq)

        # 목적지 도착
        if x == N - 1 and y == N - 1:
            return fuel

        # 이미 더 적은 연료로 방문한 경우
        if fuel > min_fuel_to[x][y]:
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < N:
                move_fuel = 1
                if arr[nx][ny] > arr[x][y]:
                    move_fuel += arr[nx][ny] - arr[x][y]

                new_fuel = fuel + move_fuel

                if new_fuel < min_fuel_to[nx][ny]:
                    min_fuel_to[nx][ny] = new_fuel
                    heappush(pq, (new_fuel, nx, ny))

    return float('inf')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()
    print(f'#{tc} {result}')