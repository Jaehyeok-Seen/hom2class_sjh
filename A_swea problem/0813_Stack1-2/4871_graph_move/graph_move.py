import sys
sys.stdin = open('4871_input.txt')

def DFS(S,G):
    global graph, visited

    if S == G:
        return 1

    visited[S] = True
    for next in range(1, V+1):
        if not visited[next] and graph[S][next]:
            if DFS(next,G):
                return 1
    return 0

"""
V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프
특정한 두개의 노드에 경로가 존재하는지 확인
노드는 1번부터
간선으로 연결되지 않은 경우도 존재
경로가 있으면 1
경로가 없으면 0
"""


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split()) # V: 노드의 개수 , E : 간선의 개수
    graph = [[False]*(V+1) for _ in range(V+1)]
    visited = [False] * (V+1)

    for _ in range(E):
        start, goal = map(int,input().split())
        graph[start][goal] = True


    S, G = map(int,input().split())   #S는 출발점 G는 도착점

    result = DFS(S,G)
    print(f'#{tc} {result}')

