
def password(list):
    while True: # 트루면 무조건 반복 돌리는거
        removed = False # while 반복 돌면서 매번 False로 초기화된다.

        for i in range(len(list)-1,-1,-1): # 제일끝에서 2번째부터 끝까지 역순으로 반복 돌리되
            if i + 1 < len(list) and list[i] == list[i+1]: # 비교는 정방향으로 그다음거와 비교
                list.pop(i+1)
                list.pop(i)
                removed = True

        if not removed: # 이번 순회에서 제거한 게 없다면
            break # 더이상 제거할 게 없으니 종료



# 이 둘은 동일하다. python에서는 not을 쓰는게 더 관습적이고 읽기 쉽다!!


import sys
sys.stdin = open('input (1).txt')

T = 10
for tc in range(1,T+1):
    n,test_list = input().split()
    N = int(n)

    Num_list = list(map(int,test_list))
    # int로 바꿔서 리스트에 담는 것 까지 완료

    # N은 몇자리인지 #list는 번호리스트
    result1 = password(Num_list)
    final_result = ''.join(map(str,result1))
    print(f'#{tc} {final_result}')

# 0~9로 이루어진 숫자 배열에서
# 같은 번호로 이루어진 쌍을 소거하면서 더이상 같은 쌍이 없다면
# 최종 비밀번호!!