"""
1
4
71 51 30 1
29 63 32 93
84 94 33 21
56 40 80 31
"""


"""
N명의 직원
일을 공평하게 배분
직원들의 번호N에다가 해야할 일에도 번호N
i번 직원이 j번 일을 하면 성고할 확률 p[i][j]
주어진 일이 모두 성공할 확률의 최댓값을 구해라
모든 일을 성공할 확률이 최대화될 때의 확률을 퍼센트 단위로 소수점 아래 7번째 자리에서 반올림하여 6번째까지 출력한다.
성공할 확률은 고정 첫번째 받는 p는 처음값
두번째 받는 p값은 
"""

# T= int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     work = []
#     for _ in range(N):
#         row = list(map(int, input().split()))
#         work.append(row)
#         # 인덱스 = 일하는 사람 -1
#     #재료 준비 완료
#     #대각선을 가로 질렀던 값들을 100으로 나눈 후 모두 곱한 값 출력
#     start_i = 0
#     start_j = 0
#     result = [ ]
#     while start_i < N and start_j < N:
#         ing = work[start_i][start_j] / 100
#         result.append(ing)
#         start_i += 1
#         start_j += 1
#         if len(result) == N:
#             break
#     final_result = result[0]
#     for i in range(1,len(result)):
#         final_result *= result[i]
#     real_result = final_result * 100
#
#
#     print(f'#{tc} {real_result:.6f}')
# ===========================================================================================
# 이해 잘 못 했었음

import sys
sys.stdin = open('input.txt')

def tracking(row, current_value):
    global max_work, job_assigned
    if row ==N:
        max_work = max (max_wrok, current_value)

def tracking(row, current_value):
    global max_work, job_assigned
    if row == N:
        max_work = max(max_work, current_value)
        return

    # 가지치기: 남은 행에서 가능한 최대값으로 상한선 계산
    upper_bound = current_value
    for i in range(row, N):
        row_max = 0
        for j in range(N):
            if not job_assigned[j]:
                row_max = max(row_max, problem_work[i][j])
        upper_bound *= (row_max / 100)

    if upper_bound <= max_work:
        return

    for work in range(N):
        if job_assigned[work]:
            continue

        job_assigned[work] = True
        new_value = current_value * (problem_work[row][work]/100)
        tracking(row+1, new_value)
        job_assigned[work] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    problem_work = [list(map(int, input().split())) for _ in range(N)]
    job_assigned = [False] * N
    max_work = -1

    tracking(0, 1)
    result = max_work * 100
    print(f'#{tc} {result:.6f}')