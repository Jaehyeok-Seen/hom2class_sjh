

def permutation(person, work):
    global max_effi
    # 종료 조건
    if person == N:
        if max_effi <work:
            max_effi = work
        return

    for j in range(N):
        if not worked[j]:
            worked[j] = True
            permutation(person + 1, work * P[person][j] * 0.01) # person +1 : 다음 선택
            worked[j] = False

import sys
sys.stdin = open('input.txt')

T= int(input())
for tc in range(1,T+1):
    N = int(input()) #직원, 일의 갯수
    P = [list(map(int,input().split())) for _ in range(N)] #일의 효율

    worked = [False] * N
    #중복 선택을 배제할 수 있도록 방문처리 배열을 생성
    max_effi = 0
    permutation(0,1) # 1인 이유는 처음은 100% 확률로 시작

    print(f'#{tc} {max_effi * 100:.06f}')
