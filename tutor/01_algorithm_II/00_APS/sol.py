import sys
sys.stdin = open('input.txt')


def search(r, acc, accK):
    global result, L
    if accK > L: return

    if r == N:
        result = max(result, acc)


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    visited = [0] * N
    search(0, 0, 0)
    print(f'#{tc} {result}')