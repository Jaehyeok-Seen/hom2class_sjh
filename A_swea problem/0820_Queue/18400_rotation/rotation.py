import sys
sys.stdin = open('5097_input.txt')

from collections import deque


"""
N개의 숫자
M: 맨앞의 숫자를 맨뒤로 보내는 작업 
그 때 맨 앞에 있는 숫자를 출력하는 프로그램
"""

T = int(input())


for tc in range(1,T+1):

    N, M = map(int,input().split())
    number_list = list(map(int,input().split()))


    queue = deque([number_list[0]]) #큐를 만들고 시작점을 넣어둠
    count = 0

    for i in range(1, M+1): #M번만큼 반복돌리기
        current = queue.popleft()

        number_list.append(current)
        number_list.pop(0)
        count += 1

        queue.append(number_list[0])

        if count == M:
            break

    print(f'#{tc} {number_list[0]}')



