import sys

sys.stdin = open('input.txt')


import heapq

def search(start, acc_dist):
    global result

    candidate = []
    # 내 지점에서 갈 수 있는 모든 후보군들을
    # 다음 조사 대상으로 삼곘다.
    for next_info in graph[start]:
        candidate.append(next_info)
    # print(candidate)
    visited[start] = 1

    heapq.heapify(candidate)
    while candidate:
        weight, now = heapq.heappop(candidate)

        # 거기 아직 방문한 적 없나요?
        if not visited[now]:
            result += weight
            visited[now] = 1
            for weight, next in graph[now]:
                if not visited[next]:
                    heapq.heappush(candidate, [weight, next])


T = int(input())
for tc in range(1, T + 1):
    # V: 노드의 개수, E: 간선의 개수
    # 단, 0부터 V까지 (V+1)
    V, E = map(int, input().split())
    # 시작노드, 끝노드, 가중치
    edges = [list(map(int, input().split())) for _ in range(E)]
    print(edges)

    result = 0  # MST 가중치의 총합
    '''
        아이디어
        집합이 뭐 어쩌구 저쩌구.. 리더라 뭐 어쩌구..
        올바른 리더가 어쩌구,.. 평탄화가 어쩌구... 난 다 모르겠고..

        그래프를 가지고 트리를 만들거라매?

        아무 노드 하나 붙잡고, 거기서 갈 수 있는것중에 제일 짧은거 하나 선택해서
        그 길로 가자.

        1. 아무 노드나 선택한다.
        2. 그 노드에서 갈 수 있는 모든 길을 일단 모두 고려한다. (후보군에 삽입)
        3. 그 후보군 들 중에 제일 짧은 일 하나 선택한다.
        4. 3번에서 선택한 도착지에서 2번을 다시한다. (후보군에 삽입)
        5. 2~4를 모든 노드를 방문할때까지 한다. 
    '''
    # print(edges)
    visited = [0] * (V + 1)
    # 그래프 정보 -> 인접 리스트로
    # {0: [], 1: [], 2: []}
    graph = {start: [] for start in range(V + 1)}
    # print(graph)
    for start, end, weight in edges:
        # start에서 갈 수 있는 모든 정보들을 모은 리스트에
        # [end까지 가는데 드는 비용, 도착 노드 번호]
        # 무 방향 그래프
        graph[start].append([weight, end])
        graph[end].append([weight, start])
    # print(graph)
    search(0, 0)

    print(f'#{tc} {result}')
