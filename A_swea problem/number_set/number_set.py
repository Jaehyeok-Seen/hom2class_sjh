# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
# N은 5 이상 50 이하
# sort로 너무 가볍게 풀었음
# import sys
# sys.stdin = open( 'input.txt')
#
# T = int(input())
# for tc in range(1, T+1):
#
#     N = int(input())
#     number_list = list(map(int,input().split()))
#     number_list.sort()
#     result = " ".join(map(str,number_list))
#     print(f'#{tc} {result}')


#선택정렬 이용하는 버전
import sys
sys.stdin = open( 'input.txt')

T = int(input())
for tc in range(1, T+1):
    #주어진 리스트 중에서 최소값을 찾기
    #그 값을 리스트 맨 앞에 위치한 값과 변경
    # 맨 처음 위치를 제외한 나머지 리스트를 대상으로 위의 과정을 반복, 2중 for문
    N = int(input())
    number_list = list(map(int, input().split()))
    result = ''
    for i in range(N-1):
        min_index = i
        for j in range(i+1,N):
            if number_list[i] > number_list[j]:
                min_index = j
                number_list[i],number_list[min_index] = number_list[min_index],number_list[i]

    result = " ".join(map(str,number_list))
    print(f'#{tc} {result}')
