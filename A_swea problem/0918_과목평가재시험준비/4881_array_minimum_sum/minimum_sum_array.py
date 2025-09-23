import sys
sys.stdin = open('sample_input (4).txt')

"""
세로줄에서 2개 이상 고를 수 없다 = 한 열에 하나씩만
최소 합을 출력하는 프로그램
"""
def recur(indx,cur_sum):
    global min_sum

    if cur_sum >= min_sum:
        return

    if indx == N:
        min_sum = min(min_sum, cur_sum)
        return
    #가지치기 연습
    remaining_sum = 0

    for next_row in range(indx+1,N): #처리 안한 행들
        min_sum_remaining = float('inf')
        for col in range(N): #모든 열에 대해서
            min_sum_remaining = min(min_sum_remaining,arr[next_row][col])

        # 열에 대해 최소 비용을 누적한다.
        remaining_sum += min_sum_remaining

    if cur_sum + remaining_sum >= min_sum:
        return

    for col in range(N):
        if visited[col]:
            continue
        visited[col] = True
        recur(indx+1, cur_sum + arr[indx][col])
        visited[col] = False

T=int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_sum = float('inf')
    visited = [False] * N
    recur(0,0)
    print(f'#{tc} {min_sum}')