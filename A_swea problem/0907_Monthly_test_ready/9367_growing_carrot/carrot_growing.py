"""
당근의 크기가 연속으로 커진 경우 그 개수를 알려준다.
당근의 크기가 수확한 순서로 주어질 때, 선별기가 알려준 연속으로 커지는 당근의 갯수(최대)
연속으로 커지지 않는 경우 최소 길이는 1이다.
"""
import sys
sys.stdin = open('carrot_sample_in.txt')

def discriminator(carrot_list):
    global count
    current_carrot = carrot_list[0]
    count_list = []

    current_count = 1
    for i in range(1,len(carrot_list)):
        if current_carrot < carrot_list[i]:
            current_carrot = carrot_list[i]
            count += 1

        else:
            count_list.append(count)
            current_carrot = carrot_list[i]
            count = 1

    count_list.append(count)
    count = max(count_list)



T=int(input())
for tc in range(1,T+1):
    N = int(input())
    count = 1
    p_carrot_list = list(map(int, input().split()))
    discriminator(p_carrot_list)
    print(f'#{tc} {count}')