import sys
sys.stdin = open('input.txt')

def recur(cur_idx,cur_sum):
    global min_diff
    if cur_idx >= N:
        if cur_sum >=B:
            min_diff= min(min_diff,abs(B - cur_sum))
        return

    recur(cur_idx + 1, cur_sum)
    recur(cur_idx + 1, cur_sum + height[cur_idx])




T=int(input())
for tc in range(1,T+1):
    N, B = map(int,input().split())
    height = list(map(int,input().split()))
    min_diff = float('inf')
    """
    탑은 1명이상으로 이루어져야한다.
    N명의 점원들의 키의 합과 같다
    높이가 B이상인 경우 너무 높으면 위험하니까, B이상이면서 높이가 가장 낮은 탑
    출력하기
    """
    recur(0,0)
    print(f'#{tc} {min_diff}')