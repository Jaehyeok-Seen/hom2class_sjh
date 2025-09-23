def quick_sort(num_list):
    if len(num_list) <= 1:
        return num_list

    pivot = num_list[0] # 기준 점은 가장 왼쪽 값을 선정
    left = []
    right = []
    for idx in range(1,len(num_list)):
        if num_list[idx] < pivot:
            left.append(num_list[idx])
        else:
            right.append(num_list[idx])

    return [*quick_sort(left), pivot, *quick_sort(right)] #새로운 리스트를 계속 만들다보니 메모리를 잡아먹는다.

import sys
sys.stdin = open('5205_input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    num_list = list(map(int,input().split()))

    result = quick_sort(num_list)

    print(f'#{tc} {result}')
