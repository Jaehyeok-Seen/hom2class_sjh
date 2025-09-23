import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N, L = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    print(data)