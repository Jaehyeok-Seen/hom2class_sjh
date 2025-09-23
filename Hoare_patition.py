def hoare_partition(arr,l,r):
    pivot = arr[l]
    i = l -1
    j = r + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i +=1
        j -= 1
        while arr[j] > pivot:
            j -= 1
            # 포인터가 교차하면 분할 완료
        if i >= j:
            return j  # 분할점 반환 (왼쪽 영역의 마지막 인덱스)

        # 잘못된 위치의 원소들을 교환
        arr[i], arr[j] = arr[j], arr[i]

def quick_sort(arr, l, r):
    if l < r:
        s = hoare_partition(arr, l, r)  # 파티션 함수 호출!
        quick_sort(arr, l, s)           # 왼쪽 재귀
        quick_sort(arr, s + 1, r)       # 오른쪽 재귀

