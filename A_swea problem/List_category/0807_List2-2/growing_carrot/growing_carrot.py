# 연속으로 커지는 당근의 수 리스트에서 최댓값을 출력하는 프로그램

def carrot_growth_discriminator(N,C):
    max_count_carrot = 1
    for i in range(N): # N개의 당근목록에서 하나씩 
        count = 1
        for j in range(i+1,N):
            if C[j] > C[j-1]:
                count += 1
                if max_count_carrot < count:
                    max_count_carrot = count    
            else: #연속으로 커지지 않을 때 다시 count =1로 리셋
                count=1
    return max_count_carrot


import sys
sys.stdin = open('carrot_sample_in.txt')

T = int(input()) # test case의 개수
for tc in range(1,T+1):
    N = int(input())  #당근 개수N개
    C = list(map(int,input().split())) #당근의 크기를 나열한 리스트
    print(f'#{tc} {carrot_growth_discriminator(N,C)}')
    
        

# 8
# 1 2 1 2 3 1 2 1