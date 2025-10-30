import sys

sys.stdin = open('input.txt')

'''
    그래프에서 사이클을 제거하고 
    모든 노드를 포함하는 트리를 구성할 때, 
    가중치의 합이 최소가 되도록 만든 경우를 
    최소신장트리라고 한다.

    0번부터 V번까지의 노드와 E개의 간선을 가진 그래프 정보가 주어질 때, 
    이 그래프로부터 최소신장트리를 구성하는 
    간선의 가중치를 모두 더해 출력 
'''
def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x = find_set(x)
    root_y = find_set(y)

    if root_x < root_y:
        parent[root_y] = root_x
    else:
        parent[root_x] = root_y



T = int(input())
for tc in range(1, T + 1):
    # V: 노드의 개수, E: 간선의 개수
    # 단, 0부터 V까지 (V+1)
    V, E = map(int, input().split())
    # 시작노드, 끝노드, 가중치
    edges = [list(map(int, input().split())) for _ in range(E)]
    print(edges)
    edges.sort(key=lambda x: x[2])

    result = 0  # MST 가중치의 총합
    '''
        아이디어2
        크루스칼이라는 아죠씨가 생각하기론...
        야 이게 그냥 방문 했냐 안헀냐 만 가지고는 안되더라
        결국 하나의 트리를 구성해야 하니
        모든 노드가 하나의 집합에 속해야 하더라....
        그래서 서로소 집합을 사용해서 검증 해야하더라
    '''
    # 각 노드들이 자신을 루트로 삼는 정보를 만든다.
    parent = list(range(V+1))

    for start, end, weight in edges:
        # 자 우리는 언제 간선에 대한 정보를 더할거냐면
        # 사이클이 형성되지 않아야 함
        # 같은 소속을 가진 노드들 끼리는 union 하면 안됨!
        if find_set(start) != find_set(end):
            union(start, end)
            result += weight

    
    print(f'#{tc} {result}')
