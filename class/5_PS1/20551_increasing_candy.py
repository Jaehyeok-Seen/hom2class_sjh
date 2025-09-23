# 증가하는 사탕 수열
# 사탕을 담은 상자
#   - A, B, C 개
#   - 순증가 (A<B<C)
#   - 각 상자는 1개 이상
#
# 목표
#   - 순증가로 만들기 위해
#     0개 이상을 먹자
#
# A상자
#   - B보다 작게
# B상자
#   - C보다 작게
# C상자 (그대로 두자)
#
# ------ 문제 읽기
#
# ------ 설계
#
# 1. 완전 탐색
# - B를 C보다 작을 때까지 하나씩 먹자
#   - A를 B보다 작을 때까지 하나씩 먹자
#
# - 이중 for 문 구현하면 9,000,000번 정도 연산발생
#   - 최악의 케이스 (3000, 3000, 3)
#
# 2. 규칙을 세우자
# - B = C - 1 / A = B - 1 로 만들면 된다.

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    # 3개 정도는 따로 받자!
    A, B, C = map(int, input().split())

    # 불가능한 케이스를 먼저 지우자
    if A < 1 or B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat_count = 0

    # B상자 = C상자 - 1 (B가 C보다 크거나 같을 때만)
    if B >= C:
        eat_count += B - (C-1)
        B = C - 1

    # A상자 = B상자 - 1 (A가 B보다 크거나 같을 때만)
    if A >= B:
        eat_count += A - (B-1)
        A = B - 1

    print(f'#{tc} {eat_count}')











