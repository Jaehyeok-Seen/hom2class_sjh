import sys
sys.stdin = open('input.txt')

"""
모든 정점을 너비우선탐색 하여 경로를 출력하시오.
시작 정점을 1로 시작하시오.
"""
from collections import deque

def BFS(Graph, start):
    global V
    visited = [False]*(V+1)
    queue = deque([start])
    path = []
    while queue:
        temp = queue.popleft()
        if not visited[temp]:
            visited[temp] = True
            path.append(temp)
            for k in Graph[temp]:
                if not visited[k]:
                    queue.append(k)
    return path

T = 1
for tc in range(1,T+1):

    V, E = map(int,input().split())
    node = list(map(int,input().split()))
    G = [[] for _ in range(V + 1)]

    for j in range(0,len(node),2):
        start = node[j]
        goal = node[j+1]

        G[start].append(goal)
        G[goal].append(start)
    print(G)
    problem_path = BFS(G,1)

    print(f'#{tc}', *problem_path)















# def BFS(G,s): #G는 그래프, s=시작점
#     global V
#     visited =[0]*(V+1)
#     result = []  # 경로만 출력할거라 빈 리스트로 지정
#     queue = []
#     queue.append(s)
#     while queue:  #첫시작을 큐에 넣고 큐가 비어있지않다면 무한반복 돌리고
#         temper = queue.pop(0) #선입선출룰에 따라 처음 인덱스 값을 템퍼에 담아두고
#         if not visited[temper]: #꺼낸 처음값이 방문학적이 없다면
#             visited[temper] = True # 방문한걸로 바꾼 후
#             result.append(temper) # 경로 출력해야하니까
#             for i in G[temper]:
#                 if not visited[i]:
#                     queue.append(i)
#     return result
#
# T = 1
# for tc in range(1,T+1):
#
#     V, E = map(int,input().split())
#     node = list(map(int,input().split()))
#     G =[[] for _ in range(V+1)]
#     for j in range(0,len(node),2):
#         start,goal = node[j],node[j+1]
#         G[start].append(goal) #방향이 없기때문에
#         G[goal].append(start) #둘다 추가
#
#     my_result = BFS(G,1)
#
#     print(f'#{tc}', *my_result)




