def partition(arr,left,right):
    pivot = arr[left]
    i = left + 1
    j = right

    while i <= j:
        #범위안에서 계속해서 반복 돌려야하니까
        while i <= j and arr[i]<= pivot:
            i +=1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i],arr[j] = arr[j],arr[i]

    arr[left],arr[j] = arr[j], arr[left]
    return j

def quick_sort(arr,left,right):
    if left < right:
        mid = partition(arr,left,right)
        quick_sort(arr,left,mid-1)
        quick_sort(arr,mid+1,right)