import sys
sys.stdin = open('input.txt')

"""
N명의 점원들
점원의 키 H
탑의 높이가 B이상인 경우 부터 출력
그러나 결과는 B와의 차이가 가장 작은 케이스(차이값을 출력) = 절대값
"""

def

T= int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    #N :직원의 수
    #B :기준 점
    info = list(map(int,input().split()))

    result = abs(B-높이)
    print(f'#{tc} {result}')

1   2   3   4   5
 1   1   1   1   1


1 2 4 5


1 4 5
2 4 5
3 4 5