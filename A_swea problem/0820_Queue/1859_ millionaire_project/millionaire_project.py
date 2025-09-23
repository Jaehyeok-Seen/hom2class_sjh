import sys
sys.stdin = open('input.txt')

from collections import deque

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    price = list(map(int,input().split()))
    my_price = price[::-1]

    gap = 0
    high = 0

    for point in my_price:
        if point > high:
            high = point
        else:
            profit = high - point
            gap += profit


    print(f'#{tc} {gap}')

    """
    임의로 최댓값을 지정 =  가격을 뒤집은 가격리스트의 처음 값으로 지정
    최대값이 반복돌려서 하나씩 꺼냈을 때의 값보다 크다면 
    반복돌린 값을 뺀 이익을 profit에 저장
    
    두번째 포인트 값이 또 작으니까
    profit에 저장 
    """






"""
1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
3. 판매는 얼마든지 할 수 있다.

예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
"""
