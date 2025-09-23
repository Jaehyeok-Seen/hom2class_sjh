import sys
sys.stdin = open('input.txt')

from collections import deque

def BFS(start,G):
    global V
    visited = [False] * (V+1)
    queue = deque([start])
    path =[]
    while queue:
        temp = queue.popleft()
        if not visited[temp]:
            visited[temp] = True
            path.append(temp)

            for nodes in G[temp]:
                if not visited[nodes]:
                    queue.append(nodes)
    return path

T = 1
for tc in range(1, T+1):
    V, E = map(int,input().split())
    path_list = list(map(int,input().split()))
    graph = [[] for _ in range(V+1)]
    for i in range(0,len(path_list),2):
        start = path_list[i]
        goal = path_list[i+1]

        graph[start].append(goal)
        graph[goal].append(start)

    result = BFS(1,graph)
    print(f'#1',*result)

    #노드들의 인덱스와 시작 1을 맞추어서 그래프 작성 완료


