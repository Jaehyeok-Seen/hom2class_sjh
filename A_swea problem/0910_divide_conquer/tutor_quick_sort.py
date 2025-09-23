import sys
sys.stdin = open('5205_input.txt')

"""
퀵 소트 구현 후 N//2 요소를 출력하자
퀵 소트
pivot 정해서
해당 pivot을 기준으로
작은 것은 pivot의 왼쪽으로
큰 것은 pivot의 오른쪽으로
왼쪽, 오른쪽을 다시 퀵 소트를 진행하면 자동적으로 정렬됨
"""
def quick_sort(arr,left,right):
    if left < right:
        mid = partition(arr, left, right)
        quick_sort(arr, left, mid -1)# 작은 파트 퀵 정렬
        quick_sort(arr,mid+1,right) #큰 파트 퀵정렬

    return arr

def partition(arr,left,right):
    pivot = arr[left]
    #pivot을 정하는 방법은 첫번째, 마지막요소, 가운데 요소, 중간값
    #왼쪽에서 오른쪽으로 이동하며 pivot보다 작은 요소를 찾는 인덱스 변수
    i = left + 1
    #오른쪽에서 왼쪽으로 이동하며 pivot보다 작은 요소를 찾는 인덱스 변수
    j = right

    while i <= j: #i가 커지는 순간이 교차되는 지점이라 종료조건
        while i <= j and pivot < arr[i]: #기준보다 큰 값을 찾으면 stop
            i += 1
        while i <=j and pivot > arr[j]:
            j -= 1

        #while의 조건으로 인해 반복이 종료된 경우라면 i, j의 위치를 바꾸면 안됨
        #즉, i와 j의 위치가 교차되었음을 의미
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]

    arr[left], arr[j] = arr[j],arr[left] #피봇의 위치를 j와 바꿈
    return j #현재 피봇의 위치

    #i와 j가 교차되면
    #j의 위치와 pivot의 위치를 교환
    #pivot을 기준으로 큰값은 i 번째 부터 시작 작은 값은 j번까찌 위치하고 있음
    #작은 값에서 마지막 요소와 pivot의 위치를 바꾸면
    #pivot의 정렬된 위치가 됨
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    sorted_arr = quick_sort(arr, 0, N - 1)
    result = sorted_arr[N // 2]  # N//2 번째 요소 출력

    print(f'#{tc} {result}')