import sys
sys.stdin = open('sample_input (1).txt')
from collections import deque

def BFS(start,goal):
    visited = [0] * 1000001
    queue = deque()

    queue.append((start,0))
    visited[start] = True

    while queue:
        cur, cnt = queue.popleft()
        #종료조건은 목표숫자가 만들어지면 종료
        if cur == goal:
            return cnt

        #4가지의 연산
        for next in (cur+1,cur-1,cur*2,cur-10):
            if 1<= next <= 100000 and not visited[next]:
                visited[next]= True
                queue.append((next,cnt+1))

    return -1



T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    """
    +1, -1, *2, -10 4가지 연산을 통해
    N -> M 이 되기까지 최소 몇번이 걸리는 지 구해라
    중간 결과도 항상 1,000,000 이하여야한다.
    1<=N, M<=1,000,000, N!=M
    """

    result = BFS(N,M)

    print(f'#{tc} {result}')
