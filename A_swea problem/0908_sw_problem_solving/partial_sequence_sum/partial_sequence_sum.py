import sys

sys.stdin = open('sample_input (2).txt')

# 전역변수들
num_list = []
K = 0

def dfs(start_idx, curr_sum):
    global num_list, K

    if curr_sum == K:
        return 1

    if curr_sum > K or start_idx >= len(num_list):
        return 0

    return (dfs(start_idx + 1, curr_sum) +
            dfs(start_idx + 1, curr_sum + num_list[start_idx]))

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    num_list = list(map(int, input().split()))

    result = dfs(0, 0)
    print(f'#{tc} {result}')

