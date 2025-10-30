"""
구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 예측하는 일을 맡았다.
모든 구름은 1분이 지날 때마다 1킬로미터씩 동쪽으로 이동한다
각 구역에 대해서 지금부터 몇 분뒤 처음으로 하늘에 구름이 오는지를 구하여라.
"""

H, W = map(int,input().split())
arr = [list(input()) for _ in range(H)]
predict = [[-1]*W for _ in range(H)]

for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            predict[i][j] = 0
            for x in range(j,W-j):
                if predict[i][j + x] == 0:
                    continue
                predict[i][j+x] += 1

        elif predict[i][j] == 0:
            continue

    print(predict)