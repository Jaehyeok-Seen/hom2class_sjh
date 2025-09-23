"""
버스 정류장은 1~5000까지
버스 노선은 N개가 있는데, 
i번째 버스 노선은 번호가 Ai이상이고
Bi 이하인 모든 정류장만을 다닌다.
p개의 버스 정류장에 대해 각 정류장에 몇 개의 버스 노선이 다니는지 구하는 프로그램
"""



# arr1 = [[0]*4 for _ in range(3)]
# arr1[1][1] = 10
# arr1[2][1] = 20
# print(arr1)
# for x in arr1:
#     print(x)

# # >>>
# [[0, 0, 0, 0], [0, 10, 0, 0], [0, 20, 0, 0]]
# [0, 0, 0, 0]
# [0, 10, 0, 0]
# [0, 20, 0, 0]

# arr2 = [[0]*4]*3  #레퍼런스 세개를 만들어라!!는 의미와 같다, 실제로는 하나의 행만 만들어지는 것
지그재그 정방향 배열

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

for i in range(3):
    if i%2 == 0 :
        for j in range(4):
            print(arr[i][j], end=' ')
    else:
        for j in range(3,-1,-1):
            print(arr[i][j], end=' ')
    print()

# arr1 = [[0]*5 for i in range(4)]

# print(arr1)
# print(len(arr1))
# print(len(arr1[0]))

# # 2차배열을 이해하기 위해 출력
# for i in range(len(arr1)):
#     for j in range(len(arr1[0])):
#         print('{0:4d}'.format(arr1[i][j],end = ''))
#     print()