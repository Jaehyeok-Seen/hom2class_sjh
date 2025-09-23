# N개의 0과 1로 이루어진 수열에서 연속한 1의 개수 중 최댓값을 출력하는 프로그램을 만드시오
# 연속하는 1의 개수의 최댓값을 구하라는 뜻

import sys
sys.stdin = open('input1.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())   #수열의 길이
    #0으로 시작하기 때문에 문자열 그대로 받아둬야한다.
    sequence = input()  #문자열 리스트 한덩어리임
    # num_list = [num for num in sequence]



    max_count = 0
    count = 0
    for str in sequence:

        if str == '1':
            count += 1

        else:
            if max_count < count:
                max_count = count
            count = 0    # count의 indentation문제로 11개중 1개가 오답이 계속 나옴
            # count를 초기화하는건 조건문 밖에서 즉 else에서 이루어져야함
    # 맨 마지막이 1로 끝나면서 count가 최대일때 잡질 못한다.
    # 그렇기 때문에 조건문을 빠져나왔을 때도 한번더 조건을 건다.
    if max_count < count:
        max_count = count
        count = 0

    print(f'#{tc} {max_count}')



