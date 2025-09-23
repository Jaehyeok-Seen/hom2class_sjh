def selection_sort(arr,N):             # 함수로 따로 정의해서 코드 카독성 좋게
    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i],arr[min_idx] = arr[min_idx],arr[i] #j쓰는 실수 하지않기, min_idx
    return arr




import sys
sys.stdin = open('sample_input (1).txt')

# T= int(input())
# for tc in range(1,T+1):
#     N = int(input())
#     num_list = list(map(int,input().split()))
#     sort_num_list = selection_sort(num_list, N)
#     result = []
#     count = 0
#     while count <10 and len(sort_num_list) > 0 : # while문이 총 10번 돌아가도록 바꿔야함!
#         count += 1
#         result.append(sort_num_list[-1])
#         sort_num_list.pop(-1)
#         if count < 10 and len(sort_num_list) > 0:
#             count += 1
#             result.append(sort_num_list[0])
#             sort_num_list.pop(0)
        
            
#     print(f'#{tc} {" ".join(map(str,result))}')
        
        
# 최적화 버전
T= int(input())
for tc in range(1,T+1):                            #
    N = int(input())
    num_list = list(map(int,input().split()))
    sort_num_list = selection_sort(num_list, N)
    result = []
    
    while len(result)<10 and len(sort_num_list) > 0 : # while문이 총 10번만 돌아가도록 바꿔야함!
        
        result.append(sort_num_list[-1])
        sort_num_list.pop(-1)

        if len(result)<10 and len(sort_num_list) > 0: # 여기서도 len길이가 0보다 클 경우만 작동되도록 이중체크
            
            result.append(sort_num_list[0])
            sort_num_list.pop(0)
        
            
    print(f'#{tc} {" ".join(map(str,result))}')

"""
3. 코드 가독성 향상

count 변수 제거로 상태 관리 단순화
조건문 중복 제거로 로직 명확화
pop() 직접 사용으로 코드 간소화

1. 조건 단순화
python# ❌ 기존: 복잡한 count 관리
count = 0
while count < 10 and len(sort_num_list) > 0:
    count += 1
    # ...
    if count < 10 and len(sort_num_list) > 0:
        count += 1
        # ...

# ✅ 최적화: result 길이로 직접 판단
while len(result) < 10 and len(sort_num_list) > 0:
    result.append(sort_num_list.pop())
    if len(result) < 10 and len(sort_num_list) > 0:
        result.append(sort_num_list.pop(0))
"""
