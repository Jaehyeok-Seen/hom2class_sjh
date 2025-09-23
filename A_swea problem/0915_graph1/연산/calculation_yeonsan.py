import sys
from collections import deque

sys.stdin = open('sample_input (1).txt')

def BFS(start,goal):
    visited = [False] * 1000001
    q = deque()
    q.append((start,0)) # 시작점, 연산횟수
    visited[start] = True

    while q:
        cur, cnt = q.popleft()

        if cur == goal:
            return cnt

        #4가지 연산
        for next in (cur+1, cur-1, cur*2, cur-10):
            if 1 <= next <= 1000000 and not visited[next]:
                visited[next] = True
                q.append((next, cnt + 1))

    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = BFS(N,M)


    print(f'#{tc} {result}')
