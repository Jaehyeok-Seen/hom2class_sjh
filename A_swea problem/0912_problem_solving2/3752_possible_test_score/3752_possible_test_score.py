import sys
sys.stdin = open('sample_input.txt')
"""
N개의 문제
배점은 다르고, 틀리면 0점, 맞으면 주어진 점수

"""
def recur(indx,current):
    global score,result_score
    if indx >= N: #문제의 개수를 주어진다.
        result_score.add(current)
        return

    recur(indx + 1, current)

    recur(indx+1, current + score[indx])




T= int(input())

for tc in range(1,T+1):
    N = int(input())
    score = list(map(int,input().split()))

    result_score = set()
    # DP 배열: dp[i] = True면 점수 i를 만들 수 있음
    max_score = sum(score)
    dp = [False] * (max_score + 1)
    dp[0] = True  # 0점은 항상 만들 수 있음 (아무것도 선택하지 않으면)

    for i in score: #각 문제에 대해서
            for j in range(max_score, i-1, -1):
                if dp[j-i]:
                    dp[j] = True

    recur(0,0)
    result = sum(dp)
    print(f'#{tc} {result}')