import sys
sys.stdin = open('input.txt')

def DFS(start):
    global graph, visited,path

    visited[start] = True
    path.append(str(start))
    for my_next in range(1, E):
        if not visited[my_next] and graph[start][my_next]:
            DFS(my_next)


tc = 1
V, E = map(int,input().split())
move_list = list(map(int,input().split()))

graph = [[False]*(V+1) for _ in range(V+1)]
visited = [False] * (V+1)
path = []

for i in range(0,len(move_list),2):
    start = move_list[i]
    goal = move_list[i+1]

    graph[start][goal] = True
    graph[goal][start] = True

print(f'#{tc}', end= " ")
DFS(1)
print("-".join(path))























# import sys
# sys.stdin = open('input.txt')
#
# def DFS(indx):
#     global visited, path
#
#
#     visited[indx] = True
#     path.append(str(indx))
#
#     for next in range(1, V+1):
#         if  not visited[next] and graph[indx][next]:
#             DFS(next)
#
#
#
# #V:정점의 개수
# #E:간선의 개수
#
# V, E = map(int,input().split())
# move_list = list(map(int,input().split()))
#
# graph = [[False]*(V+1) for _ in range(V+1)]
# visited = [False] * (V+1)
# path = []
#
# for i in range(0,len(move_list),2):
#     start = move_list[i]
#     arrive = move_list[i+1]
#
#     graph[start][arrive] = True
#     graph[arrive][start] = True
#
# print(f'#1', end=" ")
# DFS(1)
# print('-'.join(path))



