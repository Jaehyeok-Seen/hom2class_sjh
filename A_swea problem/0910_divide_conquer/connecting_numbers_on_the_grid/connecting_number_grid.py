import sys
sys.stdin = open('sample_input.txt')

def finding(arr,indx,current,i,j):
    #current = 숫자의 배열을 담아두는 그릇
    #indx = 6칸 이동

    current += str(arr[i][j]) #문자열에 시작을 먼저 담고

    di = [-1,1,0,0]
    dj = [0,0,-1,1]

    if indx == 6: # 7자리를 완성할 경우만 담아야함
        int_set.add(current)
        return


    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]

        if 0 <= ni < 4 and 0 <= nj < 4:
            finding(arr, indx+1,current,ni,nj)

    return current

T=int(input())


for tc in range(1,T+1):
    arr = [list(map(int,input().split())) for _ in range(4)]
    int_set = set()


    #시작점을 고정하지 않고 모든 경우의 수 돌려야함
    for i in range(4):
        for j in range(4):
            finding(arr,0,"", i, j)


    print(len(int_set))