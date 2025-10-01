import sys
from heapq import heappop, heappush
sys.stdin = open('sample_input.txt')


def dijkstra(start_node):
    pq = [(0,start_node)] #거리와 시작노드 담아두고 시작
    distance = [INF] * V
    distance[start_node] = 0

    while pq:
        dist,node = heappop(pq)
        if distance[node] < dist:
            continue

        for next_dist,next_node in graph[node]:
            new_dist = next_dist + dist
            if distance[next_node] <= new_dist:
                continue
            distance[next_node] = new_dist
            pq.append((new_dist,next_node))

    return distance

V, E = map(int,input().split())
INF = 26e8
graph = [[] for _ in range(V)]
for _ in range(E):
    start, end, weight = map(int,input().split())
    graph[start].append((weight,end))

result = dijkstra(0)
print(result)
