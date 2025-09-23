import sys
sys.stdin = open ('switch_sample_in.txt')
T = int(input())
for tc in range(1,T+1):
    N = int(input())                        # 전구의 길이

    before = list(map(int,input().split()))
    after = list(map(int,input().split()))
    count = 0

    for i in range(N): #인덱싱이니까 헷갈리지 않도록
        if before[i] != after[i]: # 처음으로 다른부분이발견되면 
            count += 1
            for j in range(i,N):
                if before[j] == 0:
                    before[j]=1
                else:
                    before[j] = 0
    
    print(count)















# list1 = [1,0,0,0,1]
# for i in range(5):
#     if list1[i] == 0:
#         list1[i] = 1
#     else:
#         list1[i] = 0
# print(list1)
#===========================
#정답코드
#before = list(map(int,input().split())) # 이전의 상태
    # after = list(map(int,input().split()))  # 이후의 상태
    # count = 0
    # for i in range(N):
    #     if before[i] != after[i]:           #스위치 조작의 시점이 처음으로 다른 곳의 위치에서 스위치 작동
    #         count += 1
    #         for j in range(i,N):                      #결국 몇번만에 원하는 상태 만들어냈는지 알아야하기때문에 카운트
    #             if before[j] == 0:
    #                 before[j] =1
    #             else:
    #                 before[j] = 0
        
    # result = count

    # print(f'#{tc} {result}')