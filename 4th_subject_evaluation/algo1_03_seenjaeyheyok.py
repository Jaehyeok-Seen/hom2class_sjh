def judge(arr):
    my_cnt = False
    test = 0
    for num in arr:
        if test < num:
            test=num
            my_cnt = True
        else:
            my_cnt = False
            return

    return my_cnt


T= int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    cnt =0
    result = []

    for _ in range(M):
        window = arr[:M]
        result.append(window)
        for _ in range(M):
            if arr:
                arr.pop(0)

    for i in range(len(result)):
        if judge(result[i]):
            cnt += 1

    print(f'#{tc} {cnt}')



