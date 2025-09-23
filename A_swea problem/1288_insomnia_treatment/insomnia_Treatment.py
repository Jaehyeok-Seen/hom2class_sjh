import sys
sys.stdin = open('sample_input.txt')

'''
최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 

예를 들어 N = 1295이라고 하자.

첫 번째로 N = 1295번 양을 센다. 현재 본 숫자는 1, 2, 5, 9이다.
두 번째로 2N = 2590번 양을 센다. 현재 본 숫자는 0, 2, 5, 9이다.
현재까지 본 숫자는 0, 1, 2, 5, 9이다.
세 번째로 3N = 3885번 양을 센다. 현재 본 숫자는 3, 5, 8이다.
현재까지 본 숫자는 0, 1, 2, 3, 5, 8, 9이다.
'''

T = int(input())
Num_list = [0,1,2,3,4,5,6,7,8,9]

for tc in range(1,T+1):
    N = int(input())
    result = set()

    i = 1


    while True:
        count_ship = str(N * i)
        digits = count_ship

        for digit in digits:
            result.add(digit)

        if len(result) == 10: #set형태라 렌 길이가 10이면 종료
            break

        i += 1

    print(f'#{tc} {i*N}')

