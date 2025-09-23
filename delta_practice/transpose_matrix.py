arr = [[1,2,3],[4,5,6],[7,8,9]] # 3*3행렬
print(f"원래 형태: {arr}")
for i in range(3):
    for j in range(3):
        if i < j:           # for j in range(i): 인 경우 if문이 필요없다
            arr[i][j], arr[j][i]  = arr[j][i], arr[i][j]

print(f"전치 행렬: {arr}")          