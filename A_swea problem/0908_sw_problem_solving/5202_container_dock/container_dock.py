# import sys
# sys.stdin = open('sample_input.txt')
#
# T= int(input())
# for tc in range(1,T+1):
#     N=int(input())
#
#     work = {}
#     for _ in range(N):
#         s, e = map(int,input().split())
#         work[s] = e
#
#     sorted_work = dict(sorted(work.items(), key=lambda x: x[1]))
#     print(sorted_work)
#     start_time = list(sorted_work.keys())
#     start_point = start_time[0] #제일 이른시간 시작값 설정
#     # print(first_start)
#     schedule = 0
#     # print(schedule)
#     cnt = 0
#
#     for next_time in start_time:
#         if next_time >= schedule: #처음 하역이 끝나는 시간보다 크다면
#             schedule = sorted_work[next_time] # 그다음 하역시작 시간 설정
#             print(f'다음 시작할 시간: {next_time} +1회 더')
#             cnt +=1
#         #하역 시작하고 끝마치지 못한다면
#
#
#     print(f'#{tc} {cnt}')
#==================================================처음에는 딕셔너리로 했는데 중복되는 키값이 있을경우 무시되는 경우때문 오류============
import sys

sys.stdin = open('sample_input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    work = []  # 딕셔너리 대신 리스트 사용
    for _ in range(N):
        s, e = map(int, input().split())
        work.append((s, e))
        #리스트 안에 튜플로 전달

    # 종료시간으로 정렬
    work.sort(key=lambda x: x[1])

    schedule = 0
    cnt = 0

    for start_time, end_time in work:
        if start_time >= schedule:
            schedule = end_time
            cnt += 1

    print(f'#{tc} {cnt}')