import sys
sys.stdin = open ('sample_input.txt')

#선택 정렬 후 리스트 정렬 된 곳에서 큰값 작은값 번갈아가면서 꺼내기로 시도
# 출력 예제를 보면 10 1 9 2 8 3 7 4 6 5
def selection_sort(arr,N): # arr는 리스트, N = 인자 개수
    for i in range(N-1):
        min_indx = i
        for j in range(i+1,N):
            if arr[min_indx] > arr[j]:
                min_indx = j
        arr[i],arr[min_indx] = arr[min_indx],arr[i]
    return arr

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    sort_arr = selection_sort(arr,N)
    # print(sort_arr)
    # 정렬된 리스트까지는 출력된 거 확인
    # 반복문안에서 큰값,작은값 순서대로 배열시키는 거 까지!
    result = []
    for  k in range(N):
        result.append(sort_arr[-1])
        result.append(sort_arr[0])
        sort_arr.pop(-1)
        sort_arr.pop(0)
        if sort_arr == []:
            break
    print(f'#{tc} {" ".join(map(str,result))}')