import sys
sys.stdin = open('input.txt')


def BFS(start):
    queue = [(start, 0)]
    distance[start] = 0 # 시작지점은 0

    while queue:
        # 현재 위치와 누적 거리
        now, acc_dist = queue.pop(0)

        for next in range(N+1):
            # 다음 지점이 현재 지점에서 갈 수 있다면
            if adj_matrix[now][next] != float('inf'):
                # 그 지점으로 가는데 드는 비용을 얻어서
                dist = adj_matrix[now][next]

                # 다음 지점에 나보다 빨리 온 사람이 없다면 갱신
                if acc_dist + dist < distance[next]:
                    distance[next] = acc_dist + dist
                    queue.append((next, acc_dist + dist))

T = int(input())

for tc in range(1, T+1):
    N, E = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(E)]
    '''
        아이디어.
        시작 노드 (문제에서는 항상 0)에서 갈 수 있는 모든 길들을 다 방문하면서
        이전에 온 애들보다 싼 애들로만 갱신하면 되는거 아님?
    '''
    # 거리 정보 초기화
    distance = [float('inf')] * (N+1)

    # 그래프 초기화 (이번엔 인접 리스트)
    # 가중치 정보를 리스트에 기록. 못가는 곳은 충분히 큰 값
    adj_matrix = [[float('inf')] * (N+1) for _ in range(N+1)]
    # 유향 그래프
    for start, end, weight in edges:
        adj_matrix[start][end] = weight
    # print(adj_matrix)

    # 0번 노드 시작
    BFS(0)

    print(f'#{tc} {distance[N]}')