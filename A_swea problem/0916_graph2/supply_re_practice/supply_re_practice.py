import sys
from heapq import heappop, heappush
sys.stdin = open('input (1).txt')

def dijkstra():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]

    repair_time = [[float('inf')] * N for _ in range(N)]
    repair_time[0][0] = information[0][0]

    heap = [(0,0,information[0][0])]

    while heap:
        (x,y,use_time) = heappop(heap)
        #또또 가지치기 까먹음
        if (x,y) == (N-1,N-1):
            return use_time

        if use_time > repair_time[x][y]:
            continue

        for i in range(4):
            next_i,next_j = x+dx[i], y+dy[i]

            if 0<= next_i<N and 0<= next_j < N:
                new_time = use_time + information[next_i][next_j]

                if new_time < repair_time[next_i][next_j]:
                    repair_time[next_i][next_j] = new_time
                    heappush(heap,(next_i,next_j,use_time + information[next_i][next_j]))

    return -1
T=int(input())

for tc in range(1,T+1):
    N = int(input())
    information = [list(map(int,input())) for _ in range(N)]
    result = dijkstra()
    print(f'#{tc} {result}')



    # print(f'#{tc} {}')