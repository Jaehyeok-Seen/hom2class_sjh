"""
사각형들이 겹칠 수 있다는 것 고려
직사각형들이 차지하는 면적을 구하는 프로그램
아래 x좌표 y좌표 위 x좌표 위 y좌표

"""
arr = [([0] * 100) for _ in range(100)]
cnt = 0
for _ in range(4):
    coordinate = list(map(int,input().split()))
    x1,y1,x2,y2 = coordinate

    for i in range(x1,x2):
        for j in range(y1,y2):
            if arr[i][j] != 1:
                arr[i][j] = 1
                cnt += 1

print(cnt)



