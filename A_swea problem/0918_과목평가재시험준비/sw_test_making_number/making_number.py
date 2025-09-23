# import sys
# sys.stdin = open('sample_input.txt')
#
# def calculation(start_idx,curr_sum):
#     global max_sum, min_sum, cal_pos
#     if start_idx == N:
#         max_sum = max(max_sum, curr_sum)
#         min_sum = min(min_sum, curr_sum)
#         result = abs(max_sum - min_sum)
#         return
#     if start_idx % 2 == 1:
#         #홀수에만 들어가게 되니까
#         for op in ['+', '-', '*', '/']:
#             cal_pos[start_idx] = op
#             calculation(start_idx+1, curr_sum)
#             cal_pos[start_idx] = []
#     else: #짝수인 경우에는 숫자가 들어가니까
#         cal_pos[start_idx] = num_card[start_idx//2] #숫자는 고정적으로 들어간다.
#
#
#
# T=int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     oper_cnt = list(map(int,input().split())) # +, -, *, / 순으로 갯수
#     num_card = list(map(int,input().split()))
#     max_sum = -1
#     min_sum = float('inf')
#     cal_pos = [[] for _ in range(2*N-1)]
#
#     # pass
#     #
#     # print(f'#{tc} {}')
import sys

sys.stdin = open('sample_input.txt')

# 사용한 연산자들의 리스트를 만들어서 카운트로 체크하면서 주어진 oper_cnt보다 작을때만 가능하게
def calculation(pos, curr_sum, used_operators):
    global max_sum, min_sum, num_card, oper_cnt

    # 모든 연산자를 다 사용했으면 (N-1개의 연산자)
    if pos == len(num_card):
        max_sum = max(max_sum, curr_sum)
        min_sum = min(min_sum, curr_sum)
        return

    # 선택지를 구성
    for idx, operator in enumerate(['+','-','*','/']):
        #매핑을 위한 것 연산자와 위치!
        if used_operators[idx] < oper_cnt[idx]:
            #사용가능하다는 뜻이기 때문
            #선택 + 재귀 + 백트래킹
            #연산자 선택
            used_operators[idx] += 1

            # 4. 연산 수행
            if operator == '+':
                new_sum = curr_sum + num_card[pos]
            elif operator == '-':
                new_sum = curr_sum - num_card[pos]
            elif operator == '*':
                new_sum = curr_sum * num_card[pos]
            elif operator == '/':
                # 음수 나눗셈 처리 주의
                if curr_sum < 0:
                    new_sum = -(-curr_sum // num_card[pos])
                else:
                    new_sum = curr_sum // num_card[pos]

            calculation(pos +1, new_sum, used_operators)
            used_operators[idx] -= 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    oper_cnt = list(map(int, input().split()))
    num_card = list(map(int, input().split()))

    max_sum = -float('inf')
    min_sum = float('inf')


    # 첫 번째 숫자부터 시작
    calculation(1, num_card[0], [0, 0, 0, 0])
    # curr_sum 을 첫번째 숫자로 지정해둔다.

    result = max_sum - min_sum
    print(f'#{tc} {result}')