import sys
sys.stdin = open('algo2_sample_in.txt')


def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if rank[root_x] == rank[root_y]:
        rank[root_x] += 1
        parent[root_y] = root_x
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y



T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 시작지점, 도착지점, 가중치
    edges = [list(map(int, input().split())) for _ in range(E)]
    # 크루스칼 방식으로 처리 준비할것들
    # 1. edges를 가중치 기반으로 정렬
    edges.sort(key=lambda x: x[2])
    # print(edges)
    # 서로소 집합을 union하는 방식을 구상
    # make_set -> 자기 자신을 부모로 하는 트리
    parent = list(range(V+1))   # 0번노드 쓴다.
    rank = [0] * (V+1)
    # print(parent)

    # 이제 모든 간선정보를 순서대로(가중치가 낮은 애들먼저)해서
    # 사이클이 형성되지 않도록 다 이으면 그만.
    result = 0
    for start, end, weight in edges:
        if find_set(start) != find_set(end):
            union(start, end)
            result += weight
    # print(parent)
    print(f'#{tc} {result}')