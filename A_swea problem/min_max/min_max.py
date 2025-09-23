import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1,T+1):
    N = int(input()) #숫자열의 갯수
    num = list(map(int,input().split()))

    max_num = num[0]
    min_num = num[0]

    for i in range(5):
        if max_num < num[i]:
            max_num = num[i]
        elif min_num > num[i]:
            min_num = num[i]
    
    difference = max_num - min_num
    print(f'#{tc} {difference}')