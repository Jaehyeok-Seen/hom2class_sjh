"""
첫 줄에 테스트 케이스 개수 T가 주어진다.
다음 줄부터 테스트케이스의 첫 줄에 
개수 N, 구간개수 N. (10<=N<=100, 2<=M<N)
다음 줄에 N개의 정수 ai가 주어진다. 
"""
import sys
sys.stdin = open( 'sample_input.txt' )

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())    # N,M에 값을 매핑하여 각각 부여
    number_list = list(map(int,input().split()))  #해당 숫자들을 분리해서 리스트에 담기 #2번째 3번째의 경우 정렬하지 않고 하면 값이 달라진다.
    sum_value_list = []            
 
    for i in range(N-M+1):      #범위설정 처음에 반복 생각안하고 3인경우만 해서 1번만 맞았음, 왜 N-M+1인지 고민 다시해보기 마지막 묶음의 첫번째값이 포함될 수 있도록 범위설정
        sum_value =sum(number_list[i:i+M]) # 범위만 고치고 여기는 또 안고치는 실수함, i부터 M까지 합을 구해야하는거니까 마지막 값 포함 안되니 M+i해줘야한다.+1이 아니다.
        sum_value_list.append(sum_value)
        difference = max(sum_value_list)-min(sum_value_list)
    
    print(f'#{tc} {difference}')