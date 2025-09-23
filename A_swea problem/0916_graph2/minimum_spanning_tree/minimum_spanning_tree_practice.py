import sys
import heapq

sys.stdin = open('sample_input (2).txt')

"""
첫 줄에 테스트 케이스의 개수 T가 주어지고, 테스트 케이스 별로 첫 줄에 마지막 노드번호 V와 간선의 개수 E가 주어진다.
다음 줄부터 E개의 줄에 걸쳐 간선의 양 끝 노드 n1, n2, 가중치 w가 차례로 주어진다. 
1<=T<=50, 1<=V<=1000, 1<=w<=10, 1<=E<=1000000
"""
def prim():
    visited = [False] * (V+1)
    heap = [(0,0)]
    total_weight = 0

    while heap:
        node, weight = heapq.heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += weight

        for next_node,next_weight in graph[node]:
            if not visited[next_node]:
                heapq.heappush(heap,(next_node,next_weight))
    return total_weight


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())
    graph = [[] for _ in range(V+1)]
    #인접 그래프 형성 완료
    for _ in range(E):
        n1,n2,w = map(int,input().split())
        graph[n1].append((n2,w))
        graph[n2].append((n1,w))

    result = prim()
    print(f'#{tc} {result}')