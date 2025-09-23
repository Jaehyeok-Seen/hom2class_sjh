import sys
sys.stdin = open ('sample_input.txt')


# T= int(input()) #test 갯수 입력 받아야함
# for tc in range(1,T+1):
#     N = int(input())
#     number_list = [int(char) for char in input()]
    

    

#     COUNT = [0]*10
    

#     for i in range(len(number_list)):
#         COUNT[number_list[i]] += 1
#     # # print(number_list)
#     # many_card = 0 # 가장 많은 장수를 가지는 숫자를 저장
#     # for num_fin in COUNT:
#     #     if many_card < num_fin:
#     #         many_card = num_fin
#     #         result = many_card
#     many_card = max(COUNT)

#     many_card_value = 0
#     for indx in range(10):
#         if COUNT[indx] == many_card:
#             many_card_value = indx
            

    
#     # 가장 큰 값이라고 착각 제일 많은 장수를 골라야함
#     # 2번예시처럼 모두 다같이 1장일 경우 가장 큰 값을 골라야함

    

    
#     print(f'#{tc} {many_card_value} {many_card}')

  



# print(f'#{T} {max(number_list)} {COUNT[number_list[max(number_list)]]}')








'''
DATA= [2, 2, 0, 1, 5]
COUNT = [0]*(5+1)
TEMP = [0]*5

for i in range(len(DATA)):
    COUNT[DATA[i]] += 1
for i in range(1, 5+1):
    COUNT[i] += COUNT[i-1]
for i in range(len(DATA)-1,-1,-1):
    COUNT[DATA[i]] -= 1
    TEMP[COUNT[DATA[i]]] = DATA[i]

print(TEMP)
'''
# 틀린 케이스



T= int(input()) #test 갯수 입력 받아야함
for tc in range(1,T+1):
    N = int(input())
    num_list = input()
    number_list = [int(char) for char in num_list]
    k = max(number_list)

    

    COUNT = [0]*10
    

    for i in range(len(number_list)):
        COUNT[number_list[i]] += 1
    # print(number_list)
    many_card = 0 # 가장 많은 장수를 가지는 숫자를 저장
    for num_fin in COUNT:
        if many_card < num_fin:
            many_card = num_fin
            

    many_card_value = 0
    for indx in range(len(COUNT)):
        if COUNT[indx] == many_card:
            many_card_value = indx
            

    
    # 가장 큰 값이라고 착각 제일 많은 장수를 골라야함
    # 2번예시처럼 모두 다같이 1장일 경우 가장 큰 값을 골라야함

    

    
    print(f'#{tc} {many_card_value} {many_card}')

  











