import sys
sys.stdin = open('input.txt')

def DFS(idx):

    global visited
    visited[idx] = True
    print(idx, end = " ")
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:
            dfs(next)



T = int(input())
for tc in range(1,T+1):

    graph = [[False] * (N+1) for _ in range(N+1)]
    visited = [False] * (N+1)

    for _ in range(M): #간선의 개수만큼 반복돌려서 정보를 받아오기
        a, b = map(int, input().split())
        graph[a][b] = True
        graph[b][a] = True
            # 이렇게 완료하면 2차원 행렬에 연결된 부분들을 표시완료
