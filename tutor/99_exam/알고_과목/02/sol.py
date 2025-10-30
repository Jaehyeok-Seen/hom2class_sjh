import sys
sys.stdin = open('input.txt')

def cal(now, next):
    '''
        now = x1, y1
        next = x2, y2
    '''
    # return abs(x1 - x2) + abs(y1 - y2)
    return abs(now[0] - next[0]) + abs(now[1] - next[1])

def search(r, acc, now):
    '''
        r: 현재 몇개의 사과농장을 조사했는가
        acc: 그때 누적된 비용은 얼마인가
        now: 그래서 내가 지금 어딨는가
    '''
    global result
    # 가지치기 (유망성 조사)
    if result < acc: return
    # 조사를 언제까지 할거냐?
    if r == N:  # 모든 사과 농장을 다 방문했다면
        # 다시 창고로 돌아가자
        distance = cal(now, [0, 0])
        result = min(result, acc+distance)
    else:
        # 조사를 하겠다. -> 모든 사과 농장을 다 방문했는지를 물어보겠다.
        # 전수 조사
        for i in range(N):
            if not visited[i]:  # i번째 농장을 방문한 적이 없다면,
                # 방문을 한다는 행위 -> 현재 위치에서, i번째 위치까지 가는데 걸리는 비용을 알아야한다.
                distance = cal(now, data[i])
                visited[i] = 1  # 간다?
                search(r+1, acc+distance, data[i])
                visited[i] = 0  # 없었던일. 0번으로 간적 없는척

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 각 사과농장 0번 1번 2번을 방문했는지 도장을 찍기위한 리스트를 하나 만든다.
    # 처음에는 전부 방문한 적 없으니 0 으로 초기화 한다.
    visited = [0] * N
    result = float('inf')   # 충분히 큰 값
    search(0, 0, [0, 0])
    print(f'#{tc} {result}')