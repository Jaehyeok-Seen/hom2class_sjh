"""
조건 1. 각 숫자의 자리수가 증가하는 수
조건 2. 그 중 곱의 값도 단조 증가하는 수여야 한다.
"""

def judge(number):
    string_list = str(number)
    for i in range(len(string_list)-1):
        if string_list[i] > string_list[i+1]:
            return False
    return True

import sys
sys.stdin = open('s_input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    A = list(map(int,input().split()))

    max_value = -1

    for i in range(N):
        for j in range(i+1, N):
            value = A[i] * A[j]

            if judge(value):
                max_value = max(max_value, value)


    print(f'#{tc} {max_value}')

