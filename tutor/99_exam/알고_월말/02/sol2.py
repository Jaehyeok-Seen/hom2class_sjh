import sys
sys.stdin = open('algo2_sample_in.txt')


def search(node):
    global result
    # 이 시작노드에서 갈 수 있는 모든 간선들을 전부 후보군에 등록
    candidate = [[weight, next] for weight, next in graph[node]]
    visited[node] = 1

    while candidate:    # 전수 조사
        # 우선순위 큐를 쓸 수가 없네?
        # 그럼 뭐.. 직접 찾아야지
        min_idx, min_weight = 0, float('inf')   # 충분히 큰 값
        # 내 후보군들 속에서 다음으로 쓸 진짜 후보군 (가장 우선순위가 높은 친구)
        for idx, item in enumerate(candidate):
            # 내가 충분히 작다고 생각했던 가중치보다 작은애를 찾으면
            if min_weight > item[0]:
                min_weight = item[0] # 가중치와
                min_idx = idx       # 그 간선의 위치를 갱신
        # 전수 조사 끝났네? 그럼이제 뭐한다?
        # 아까 찾은 진짜 제일 작은애를 뽑는다.
        weight, now = candidate.pop(min_idx)
        if visited[now]: continue   # 진짜 후보군인줄 알았는데 이미 방문한적 있으면 skip
        # 아직 방문한적 없어?
        visited[now] = 1
        result += weight

        # 그럼 이제 now번째 방문했으니, now번째에서 갈수 있는 다음 후보군도 추가
        for weight, next in graph[now]:
            if not visited[next]:
                candidate.append([weight, next])


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