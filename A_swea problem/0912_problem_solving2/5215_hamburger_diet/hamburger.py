"""
정해진 칼로리를 넘지 않게
재료는 정해진대로
재료에대한 칼로리가 주어졌을 때
정해진 칼로리 이하의 조합중에서 가장 선호하는 햄버거 조합
같은 재료 여러번 사용x , 점수의 합
used, 맛에대한 최댓값
"""
def recur(indx,curr_cal,taste):
    global min_cal, max_taste
    if indx == N: #재료를 다 사용한다면
        if curr_cal <= L:
            max_taste = max(max_taste, taste)
        return

    #포함한 경우 칼로리값 더해주고 선호도 점수도 최대를 찾아야하니까

    recur(indx+1, curr_cal + prefer[indx][1], taste + prefer[indx][0])
    recur(indx+1, curr_cal,taste)



import sys
sys.stdin = open('sample_input.txt')

T= int(input())
for tc in range(1,T+1):
    N, L = map(int,input().split())
    prefer = []
    #재료의 수 N, 칼로리 L
    for _ in range(N):
        T, K = map(int,input().split())
        prefer.append((T,K))


    # min_cal = float('inf')
    max_taste = 0

    recur(0,0,0)

    print(f'#{tc} {max_taste}')
