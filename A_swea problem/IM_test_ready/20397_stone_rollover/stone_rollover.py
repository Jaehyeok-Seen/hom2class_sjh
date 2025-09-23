import sys
sys.stdin = open('sample_in.txt')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    #N = 돌의 수, M = 뒤집기 횟수
    stone = input().split()
    for _ in range(M):
        i,j = map(int,input().split())

        # i = 기준 돌 (index가 1부터다 = 인덱싱 이용하려면 i-1이 기본)
        # j = 마주보는 돌의 갯수 (범위 넘어가면 그 즉시 종료)
    #M의 횟수에 따라 반복이 달라지고 stone을 변경시켜야함
        center = i-1

        for k in range(1,j+1): #뒤집기 횟수는 0부터 시작해서 j까지
            left = center-k
            right = center+k
            if left >=0 and right < N:
                if stone[left] == stone[right]: #숫자가 같다면 뒤집기 실시
                    if stone[left] == '1':
                        stone[left] = '0'
                        stone[right] = '0'
                    elif stone[left] == '0':
                        stone[left] = '1'
                        stone[right] = '1'
            else:
                break
    result = ' '.join(stone)
    print(f'#{tc} {result}')
