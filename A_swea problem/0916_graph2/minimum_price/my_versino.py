import sys
sys.stdin = open('sample_input.txt')
from heapq import heappush,heappop

def dijkstra():
    pq = []
    heappush(pq,(0,0,0))
    min_fuel_to = [[float('inf')] * N for _ in range(N)]
    min_fuel_to[0][0] = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while pq:
        fuel,x,y = heappop(pq)

        if x == N -1 and y == N-1:
            return fuel

        if fuel > min_fuel_to[x][y]
            continue

        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]


    return float('inf')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    result = dijkstra()