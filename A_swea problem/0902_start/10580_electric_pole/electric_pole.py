"""
문제 접근 방법:
값이 0인 이차원 행렬을 만들어 둔다.
열값이 0인 케이스는 전부 A기둥
열값이 3인 케이스는 전부 B기둥

주어지는  Ai,Bi의 값들을 1로 바꾼다.
델타 탐색을 통해 Ai Bi까지 탐색을 한다.
주어지는 N개의 각 케이스에서 델타 탐색값중 같은 값이 존재하면 2로 변경하면서 count + 1 한다.

여기서 드는 생각 그럼 열의 개수를 어떻게 정해야할까?

"""


"""
2번째 문제 접근 방법:
범위를 통해서 교차점의 개수를 내가 지정해주는 방식
주어지는 Ai Bi의 값 중 최대값을 끝범위로 지정해서 리스트를 만드는거야 A리스트 B리스트
그랬을 때 조건으로 처음 값을 기준으로 둘다 크면 교차점이 안생기고 , 둘 다 작아도 안생긴다.
즉 A랑 B중 하나라도 기준되는 값보다 작은게 있어야 교차점이 생긴다는 부분을 통해 

5개의 전선이 있다면 기준비교 대상을 하나 잡고 다 반복 돌리고 
5개 전선 반복 다돌리면 되는 거아닐까?
"""

# 주어지는게 Ai Bi이렇게 쌍으로 주어진다.

import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = [[0] for _ in range(N+1)]
    B = [[0] for _ in range(N + 1)]


    for i in range(1,N+1):
        A[i], B[i] = map(int,input().split())

    #====================교차점 구하는 조건================
    # 기준이 되는 A[k], B[k]를 잡아두고 비교하는 포문 만들어야함
    # 임의로 k = 1일때를 기준으로 비교해보자
    count = 0
    for j in range(1,N+1):
        standard_A = A[j] # 1, 2, 3, ... , N
        standard_B = B[j]



        for k in range(j+1,N+1):
            if standard_A >= A[k] and standard_B >= B[k]:
                pass
            elif standard_A <= A[k] and standard_B <= B[k]:
                pass
            else:
                count += 1

    print(f'#{tc} {count}')




