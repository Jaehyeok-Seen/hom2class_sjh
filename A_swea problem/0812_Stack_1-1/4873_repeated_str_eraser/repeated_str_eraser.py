"""
문자열 s에서 반복된 문자를 지우려고한다.
지우고 나서 다시 앞뒤 연결, 이때 또 반복문자 생기면 지운다.

다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
CAA 연속 문자 AA를 지운다.
C 1글자가 남았으므로 1을 리턴한다.
"""
import sys
sys.stdin = open('4873_input.txt')
T = int(input())
for tc in range(1,T+1):
    str_list = list(input())
    stack = []

# ================정석적인 방법
    for test in str_list:
        if stack and stack[-1] == test:
            stack.pop()
        else:
            stack.append(test)

    print(f'#{tc} {len(stack)}')

    # for test in str_list:
    #     if stack and stack[-1] != test:
    #         stack.append(test)
    #
    #     elif stack and stack[-1] == test:
    #         stack.pop()
    #     else:
    #         stack.append(test)
    #
    # print(f'#{tc} {len(stack)}')


#======================나만의 방법===
# T = int(input())
# for tc in range(1,T+1):
#     str_list = list(input())
#     stack = []
#
#     for test in str_list:
#         if test not in stack:
#             stack.append(test)
#
#         else:
#             if stack[-1] == test:
#                 stack.pop()
#             else:
#                 stack.append(test)
#
#     print(f'#{tc} {len(stack)}')








# import sys
# sys.stdin = open('4873_input.txt')
#
# T = int(input())
# for tc in range(1,T+1):
#     s = list(input())
#
#     #=========stack만들기 및 초기화
#     stack = []
#     for str in s:
#         if len(stack) != 0 and stack[-1] == str:
#             stack.pop()
#         else:
#             stack.append(str)
#
#     print(f'#{tc} {len(stack)}')
