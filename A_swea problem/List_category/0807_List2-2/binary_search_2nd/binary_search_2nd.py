# 문제설명
# 짝을 이룬 A,B 두명에게 교과에서 각자 찾을 쪽 번호 알려주면,
# 이진 탐색만으로 페이지를 찾아서 펼치면 이기는 게임

# 찾는 페이지가 c
# 시작범위 l
# 끝범위 r

import sys
sys.stdin = open('sample_input.txt')

def binary_search(N,Key): # N= 몇개의 인자를 가지는지, Key : 찾아야할 값
    start = 1
    end = N
    count = 0
    while start <= end:
        middle = (start + end) // 2
        count += 1
        if middle == Key:
            return count
        elif middle > Key:
            end = middle- 1
        else:
            start = middle + 1
    


T = int(input())


for tc in range(1, T+1):
    # page는 1부터 1000까지
    # Pa = a가 찾을 페이지 , Pb = b가 찾을 페이지
    
    # print(P,Pa,Pb) [400, 300, 350] [1000, 299, 578] [1000, 222, 888]
    P,Pa,Pb = map(int,input().split())
    A_count = binary_search(P,Pa)
    B_count = binary_search(P,Pb)

    if A_count > B_count:
        print(f'#{tc} B')

    elif A_count < B_count:
        print(f'#{tc} A')
        
    else:
        print(f'#{tc} 0')