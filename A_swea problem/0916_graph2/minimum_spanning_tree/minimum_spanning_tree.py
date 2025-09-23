import sys
import heapq
sys.stdin = open('sample_input (2).txt')

def prim_mst():
    visited = [False] * (V+1)
    min_heap = [(0,0)] #가중치, 노드
    total_weight = 0

    while min_heap:
        weight,node = heapq.heappop(min_heap)

        if visited[node]:
            continue

        visited[node] = True
        total_weight += weight

        for next_node,next_weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(min_heap,(next_weight,next_node))

    return total_weight

T=int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    graph = [[] for _ in range(V+1)]

    for _ in range(E):
        n1,n2,w = map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))    #무방향이기 때문에

    result = prim_mst()

    print(f'#{tc} {result}')