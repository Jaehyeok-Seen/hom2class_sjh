
# ### Delta 개념 부분 ####

# di = [-1,1,0,0] # 행의 변화량
# dj = [0,0,-1,1] # 열의 변화량

# for k in range(4):  # k = 0,1,2,3
#     ni = i + di[k] # k번째 방향의 행 변화량 적용
#     nj = j + dj[k] # k번째 방향의 열 변화량 적용

# """
# # k는 단순히 인덱스 번호
# # k=0일 때: di[0]=-1, dj[0]=0  → 상
# # k=1일 때: di[1]=1,  dj[1]=0  → 하  
# # k=2일 때: di[2]=0,  dj[2]=-1 → 좌
# # k=3일 때: di[3]=0,  dj[3]=1  → 우
# """
# "========================================================="

# ### 실제 동작 - di랑 dj를 따로 분리한 case ###

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

i, j = 2, 3         #현재 위치를 2,3이라고 할당

for k in range(4):
    ni = i + di[k]
    nj = j + dj[k]

    print(f" k={k} :  di[{k}]: {di[k]}, dj[{k}] = {dj[k]}")
    print(f"    ({i},{j}) +  ({di[k]},{dj[k]}) = ({ni},{nj})")
    
    #방향 판별
    if di[k] == -1: print("   → 상")
    elif di[k] == 1: print("   → 하")
    elif dj[k] == -1: print("   → 좌")
    elif dj[k] == 1: print("   → 우")
    print()


### 실제 동작 - di랑 dj를 합친 case ###

i, j = 2, 3

for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
    ni, nj = i+di, j+dj
    print(ni, nj)



N=4
for i in range(N):
    for j in range(N):
        for di, dj in [[-1,0],[1,0],[0,-1],[0,1]]:
            ni, nj =  i+di, j+dj
    print(ni,nj)
