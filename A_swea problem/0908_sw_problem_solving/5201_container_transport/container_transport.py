import sys
sys.stdin = open('5201_input.txt')

T= int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    #N개의 화물에 대한 중량
    weight = list(map(int,input().split()))
    #M개 트럭의 적재용량
    limit = list(map(int,input().split()))

    weight.sort(reverse=True)
    limit.sort(reverse=True)
    x=0
    if len(limit)>= len(weight):
        x = len(limit) - len(weight)

        for i in range(x):
            limit.pop()
    else:
        x = len(weight) - len(limit)

        for i in range(x):
            weight.pop()

    #트럭과 컨테이너가 1대 1매칭이기때문에 트럭의 인덱스 값이 컨테이너 인덱스 값보다 높은 경우 화물의 값을 변수에 담아둔다.
    result = 0 #총 옮긴 양


    re_truck = []
    re_weight = []
    for i in range(len(weight)): #트럭이 많아도 의미 없기때문
        if limit[i] >= weight[i]:
            # print(f'이번케이스에서 옮길 리스트: {weight}')
            # print(f'컨테이너 적재 한계 : {limit}')
            # print(f'컨테이너가 이번에 옮긴 양:{weight[i]}')
            result += weight[i]
        else: #옮길 수 있는 화물차가 남는 상황
            re_truck.append(limit[i])
            re_weight.append(weight[i])

    re_weight.sort()
    if re_truck and re_weight:
        for i in range(len(re_weight)):
            if re_truck[i]>=re_weight[i]:
                result += re_weight[i]

    print(f'#{tc} {result}')

