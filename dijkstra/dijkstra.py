import sys
sys.stdin = open('sample_input.txt')

from heapq import heappop,heappush

#마지막으로 함수 정의하면 끝
def dijkstra(start_node):
    pq = [(0,start_node)] # 누적거리, 노드번호
    distance = [INF] * V #각 정점까지의 최단거리를 저장할 리스트
    distance[start_node] = 0 # 시작노드 최단거리는 0으로 설정

    while pq:
        dist, node = heappop(pq)

        if distance[node] < dist:
            continue # 꺼냈을 때의 값이 기록된 값보다 크다면 버림

        #그 다음으로 어떻게 진행할 것인가?
        for next_dist, next_node in graph[node]:
            # 다음 노드로 가기 위한 누적 거리
            # 누적 거리 = 현재까지의 거리 + 다음 거리
            new_dist = dist + next_dist #거리가 누적되어야하니까
            print(next_dist, next_node) #디버깅용으로 다음 노드와 거리가 나오는지
            # 이미 작거나 같은 가중치로 온 적이 있다면 continue
            if  distance[next_node] <= new_dist:
                continue
            #큐에 넣기전에 기록 먼저
            #누적거리와 새로운 노드를 pq에 저장 + dist 갱신
            distance[next_node] = new_dist
            heappush(pq, (new_dist,next_node))

    return distance

#무한대를 설정(문제의 최대 포함) - 21억을 넘지 않는다고 가정
INF = int(21e8)

V,E = map(int, input().split())
start_node = 0
# 인접행렬로 해도 되지만 인접리스트로 진행
graph = [[] for _ in range(V)]

#간선리스트를 받아와야하니까
for _ in range(E):
    start, end, weight = map(int, input().split())
    graph[start].append((weight, end)) #다익스트리아는 단반향이다.
# 출발지로부터 모든 최단거리
result = dijkstra(0)
print(result)