import sys
sys.stdin = open('5102_input.txt')
#
from collections import deque



#

"""
첫 줄에 테스트 케이스 T
다음 첫 줄에 V와 E (V는 정점의 개수 E는 간선의 개수)
E개의 줄에 걸쳐, 간선의 양쪽 노드 번호 주어진다.
E개의 줄 이후에는 출발 노드 S와 도착 노드 G가 주어진다.
문제의 답은 S -> 도착노드G까지 간선의 수를 출력하는 것
"""


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())

    direct = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for _ in range(E):
        x,y = map(int,input().split())
        direct[x].append(y)
        direct[y].append(x)
    # print(direct)
    problem_s, problem_g = map(int, input().split())

    result = -1

    queue = deque([problem_s])
    visited[problem_s] = 1
    found = False
    while queue:
        curr = queue.popleft()

        if curr == problem_g:
            found = True
            result = visited[curr] - 1
            break

        for l in direct[curr]:
            if visited[l] == 0:
                visited[l] = visited[curr] + 1
                queue.append(l)


    if not found:
        result = 0

    print(f'#{tc} {result}')











    # print(f'#{tc} {result}')






