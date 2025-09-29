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

T = int(input())
for tc in range(1, T+1):
    # V: 노드의 개수, E: 간선의 개수
    # 단, 0부터 V까지 (V+1)
    V, E = map(int, input().split())
    # 시작노드, 끝노드, 가중치
    edges = [list(map(int, input().split())) for _ in range(E)]
    print(edges)

    result = 0  # MST 가중치의 총합
    '''
        아이디어
        어쩃든... 결국 모든 노를 다 써야 하네?
        최소 신장 트리를 만족하려면 모든 노드를 방문헀다는 뭔가가 잇어야겠네?
        
        가중치가 제일 작아야한다, 전체합이
        그럼... 뭐 더도말고 덜도말고 그냥 가중치가 제일 작은애들부터 더해보면안댐?
        대신에, 사이클을 이루지 않아야하고,
        모든 노드를 방문 해야함.
    '''
    # 가중치 기준으로 정렬을 해
    edges.sort(key=lambda x: x[2])
    # print(edges)
    visited = [0] * (V+1)

    # 모든 간선 정보 기반으로 조사를 해보자
    for start, end, weight in edges:
        # print(start, end, weight)
        # 시작노드를 방문한적 없거나,
        # 도착노드를 방문한적 없거나나
        if not visited[start] or not visited[end]:
            visited[start] = 1
            visited[end] = 1
            result += weight

    print(f'#{tc} {result}')
