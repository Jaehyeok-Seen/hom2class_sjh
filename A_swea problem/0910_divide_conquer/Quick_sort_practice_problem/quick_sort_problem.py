import sys
sys.stdin = open('input (1).txt')

def partition(arr,left,right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i<=j:
        while i<=j and arr[i]<=pivot:
            i += 1
        while i<=j and arr[j]>pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j], arr[i]

    arr[left],arr[j] = arr[j],arr[left]
    return j

def quick_sort(arr,left,right):
    if left < right:
        mid = partition(arr,left,right)
        quick_sort(arr,left,mid-1)
        quick_sort(arr,mid+1,right)

    return arr

T=int(input())
for tc in range(1,T+1):
    arr = list(map(int,input().split()))
    quick_sort(arr,0, len(arr)-1)

    print(f'#{tc}', *arr)