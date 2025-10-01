import sys
sys.stdin = open('sample_input (2).txt')


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    root_x = find(x)
    root_y = find(y)

    if rank[root_x] == rank[root_y]:
        rank[root_x] += 1
        parent[root_y] = root_x
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y


T = int(input())
for tc in range(1, T+1):
    V, E = map(int,input().split())
    edges = [list(map(int,input().split())) for _ in range(E)]
    edges.sort(key= lambda x:x[2])
    parent = [i for i in range(V+1)]
    rank = [0] * (V+1)

    result = 0
    for edge in edges:
        n1, n2, w = edge
        if find(n1) != find(n2):
            union(n1,n2)
            result += w
    print(f'#{tc} {result}')