# 최고 높이 상자를 최저점으로 옮기기
# 평탄화가 끝나면, 최대 높이인 지점과 최저 높이인 지점의 차이가 최대 1이내다
# 평탄화를 위해 옮기는 작업 횟수에 제한이 걸려있을 때, 제한된 횟수만 진행한 후 차이값이 결과값
# 가장 높은 곳에서 가장 낮은 곳으로 옮기는 작업을 덤프라고 함
#  가로길이는 무조건100, 덤프 횟수는 1이상 1000이하

import sys
sys.stdin = open('input (1).txt')

for tc in range(1,11): # 테스트 케이스 반복문
    dump_C = int(input()) # 덤프 횟수 지정
    box = list(map(int,input().split()))  # 박스 숫자들 받아와서 리스트로 담아두기
    
    for i in range(dump_C): # 100개의 숫자가 있더라도 범프 횟수 제한이 있으니까 제일 큰 범위는 범프횟수 내 반복
        max_val = box[0] # 임의 설정 최대값
        min_val = box[0] # 임의 설정 최소값
        max_idx = 0 #임의 설정 인덱스값
        min_idx = 0 #임의 설정 인덱스 값

       
        for j in range(1,100): #실제로 임의 설정 값이 맞는지 우선적으로 비교해야하기 때문에 안쪽 for문 작성
            if max_val < box[j]:
                max_val = box[j]
                max_idx = j
            if min_val > box[j] :
                min_val = box[j]
                min_idx = j
    
        box[max_idx] -= 1  #실질적인 덤프 과정(옮기기)
        box[min_idx] += 1  #실질적인 덤프 과정(쌓기)

        if max_val - min_val <= 1:
            break

    difference = max_val - min_val
    print(f'#{tc} {difference}')




##1 11
#2 30
#3 52
#4 23
#5 85
#6 13
#7 37
#8 24
#9 11
#10 27
"""
계속해서 2만큼 작게 나온다 6번케이스의 경우에는 1이 작게 나오는 오답 반복
==============================================
오답 코드
import sys
sys.stdin = open('input (1).txt')

for tc in range(1,11): # 테스트 케이스 반복문
    dump_C = int(input()) # 덤프 횟수 지정
    box = list(map(int,input().split()))  # 박스 숫자들 받아와서 리스트로 담아두기
    
    for i in range(dump_C): # 100개의 숫자가 있더라도 범프 횟수 제한이 있으니까 제일 큰 범위는 범프횟수 내 반복
        max_val = box[0] # 임의 설정 최대값
        min_val = box[0] # 임의 설정 최소값
        max_idx = 0 #임의 설정 인덱스값
        min_idx = 0 #임의 설정 인덱스 값

       
        for j in range(100): #실제로 임의 설정 값이 맞는지 우선적으로 비교해야하기 때문에 안쪽 for문 작성
            if max_val < box[j]:
                max_val = box[j]
                max_idx = j
            if min_val > box[j] :
                min_val = box[j]
                min_idx = j
        
        box[max_idx] -= 1  #실질적인 덤프 과정(옮기기)
        box[min_idx] += 1  #실질적인 덤프 과정(쌓기)

        difference = box[max_idx] - box[min_idx]   # 이부분 덤프 전 변수를 사용하니까 자꾸 안맞음

    if difference <= 1:
        break

    print(f'#{tc} {difference}')

"""

"""
왜 이런 오차가 반복되는가
덤프 한 번 하면 max_idx나 min_idx에 해당하는 칸이
더 이상 최고/최저가 아닐 수 있음

그런데 차이 계산할 때 여전히 예전 인덱스를 써서
현재 박스 상태 기준이 아닌 옛날 위치 차이를 계산함

덤프 횟수가 많아질수록 이런 오차가 누적돼서
케이스에 따라 1~2 차이 나는 결과가 생김
"""