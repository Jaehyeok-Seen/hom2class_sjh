"""
자릿수에 따라 24자리이면 2진수를 16진수로, 6자리이면 16진수를 2진수로 변환하는 프로그램 작성

16진수 E6D의 각 자리를 4비트 2진수로 변경하면 다음과 같다.

16진수 01은 00000001로 표시되고, 16진수  00은 00000000으로 표시된다.

2진수는 0과 1로
16진수는 알파벳 대문자와 숫자
"""

import sys
sys.stdin = open('sample_input.txt')

T=int(input())
for tc in range(1,T+1):
    information= list(input().split())
    jinbub = int(information[0])
    num_list = information[1]

    if jinbub == 24: # 24일 경우 2진수를 16진수로 변환
        decimal = int(num_list,2)
        result = hex(decimal)
        print(f'#{tc} {result[2:].upper()}')

    elif jinbub == 6: # 16진수를 2진수로 변환하는 프로그램 작성
        decimal = int(num_list,16)
        result = bin(decimal)[2:]
        print(result.zfill(4 * len(num_list)))  # 각 16진수 자릿수 = 4비트

        my_list =[]
        for i in range(len(num_list)):
            my_list.append(bin(int(num_list[i],16))[2:].zfill(4))
        print(''.join(map(str,my_list)))
    # print(num_list)


    #
    # print(f'#{tc} {}')