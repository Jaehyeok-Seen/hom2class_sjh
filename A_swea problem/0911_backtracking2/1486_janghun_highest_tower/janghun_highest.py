"""
N명의 직원
B인 선반의 높이
H 직원들의 키
탑은 점원 1명 이상
높이가 B이상이지만 그중 가장 낮은 탑

"""
def recur(indx,curr):
    global H,B,N, min_height
    if curr >= B:
        min_height = min(min_height, curr)
        return

    if indx == N:
        return

    recur(indx+1,curr)
    recur(indx+1, curr + H[indx])


import sys
sys.stdin = open('input.txt')
T=int(input())

for tc in range(1,T+1):
    N, B = map(int,input().split())
    H = list(map(int,input().split()))

    #H의 조합으로 더해진 합을 담을 그릇
    min_height = float('inf')

    recur(0,0)
    result =abs(B - min_height)
    print(f'#{tc} {result}')