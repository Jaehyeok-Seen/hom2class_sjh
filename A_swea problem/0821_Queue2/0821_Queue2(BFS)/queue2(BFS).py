"""
두개의 정점 사이의 간선을 순서대로 나열 한 것
시작 정점은 1
모든 정점을 너비 우선탐색 = BFS로 하여 경로 출력
첫줄은 정점의 개수 V와 간선의 개수 E가 주어진다.
"""
# import sys
# sys.stdin = open('input.txt')
#
# from collections import deque
#
# V, E = map(int,input().split())
# information = list(map(int,input().split()))
#
# Queue = deque([1])
#
# visited = [0] * V
#
# for i, i+1 in range(1,V+1,2):
#     list = i, i+1
#=====================================================================================
def bfs(s, V):  # 시작정점 s, 마지막 정점 V
    경로 = []
    queue = []
    queue.append(s)
    visited = [False]*(V+1)
    visited[s] = True

    while queue:
        temp = queue.pop(0)
        경로.append(temp)
        for node in adj_l[temp]:
            if visited[node] == False:
                queue.append(node)
                visited[node] = True

V, E = map(int, input().split()) # 1번부터 V번 정점, E개의 간선
arr = list(map(int, input().split()))



# 인접리스트 -------------------------
adj_l = [[] for _ in range(V+1)]
for i in range(E):
    v1, v2 = arr[i*2], arr[i*2+1]
    adj_l[v1].append(v2)
    adj_l[v2].append(v1)    # 방향이 없는 경우
# 여기까지 인접리스트 -----------------
bfs(1, 7)




