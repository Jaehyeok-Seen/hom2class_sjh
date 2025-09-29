import sys
sys.stdin = open('algo2_sample_in.txt')


import heapq

def search(node):
    global result
    # 이 시작노드에서 갈 수 있는 모든 간선들을 전부 후보군에 등록
    candidate = [[weight, next] for weight, next in graph[node]]
    visited[node] = 1

    # 내 후보군 리스트를 우선순위 큐로 변환
    heapq.heapify(candidate)
    while candidate:    # 전수 조사
        # 우선순위큐에서 가장 우선순위가 높은(가중치가 제일 낮은)
        weight, now = heapq.heappop(candidate)
        if visited[now]: continue   # 진짜 후보군인줄 알았는데 이미 방문한적 있으면 skip
        # 아직 방문한적 없어?
        visited[now] = 1
        result += weight

        # 그럼 이제 now번째 방문했으니, now번째에서 갈수 있는 다음 후보군도 추가
        for weight, next in graph[now]:
            if not visited[next]:
                heapq.heappush(candidate, [weight, next])


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 시작지점, 도착지점, 가중치
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 그래프를 직접 그려서, 한땀한땀 조사한다.
    graph = {v: [] for v in range(V+1)}
    # 무방향 그래프
    for start, end, weight in edges:
        graph[start].append([weight, end])
        graph[end].append([weight, start])
    visited = [0] * (V+1)
    result = 0
    # MST라는건 모든 노드가 다 이어진 (하지만 가중치의 합이 최소인)
    search(0)
    print(f'#{tc} {result}')