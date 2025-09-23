import sys
sys.stdin = open('5207_input.txt')
def binary_search(arr,target):
    left = 0
    right = len(arr)-1 #인덱스니까 맞추기 위해tj

    while left <= right:
        mid = (left+right) //2

        if arr[mid] == target:
            return mid

        elif arr[mid]  < target:
            left = mid +1

        else:
            right = mid - 1

    return -1

T=int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int, input().split()))

    count = 0

    for target in B:
        result = binary_search(A,target)
        if result != -1:
            count += 1

    print(f'#{tc} {count}')