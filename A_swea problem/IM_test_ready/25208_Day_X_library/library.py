"""
도서관의 불편도가 최소가 되도록 배치해야한다
불편도 = 책의 인기도 x 책이 꽂힌 층수
책은 항상 가장 아래층인 1층부터 차곡차곡 꽂는 것을 원칙으로 한다.
최적의 방법으로 책을 배치했을 때의 최소 총 불편도를 계산하는 프로그램 작성
문제 : 최소 총 불편도를 계산하라
"""

import sys
sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    #N = 책의 개수
    #M = 책장의 개수
    level = list(map(int,input().split()))
    level.sort()
    #책장의 층수
    prefer = list(map(int,input().split()))
    prefer.sort(reverse = True)
    #책의 선호도
    # print(level)
    # print(prefer)
    height_list = []
    for x in level:
        for k in range(1,x+1):
            height_list.append(k)
    height_list.sort()

    total = 0
    for i in range(N):
        total += height_list[i]*prefer[i]

    print(f'#{tc} {total}')
