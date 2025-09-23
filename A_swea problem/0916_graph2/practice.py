from collections import deque

def BFS(start,goal):
    visited = [False]*1000001
    queue = deque()
    queue.append((start,0))
    visited[start] = True

    while queue:
        current, cnt = queue.popleft()

        if current == goal:
            return cnt

        for next in (current+1,current-1,current*2,current-10):
            if 1<=next<=1000000 and not visited[next]:
                visited[next] = True
                queue.append((next,cnt+1))
    return -1


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    result = BFS(N,M)


    print(f'#{tc} {result}')
