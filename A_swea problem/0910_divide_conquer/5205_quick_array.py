import sys
sys.stdin = open('5205_input.txt')

"""
퀵정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력하는 프로그램
"""
def quick_sort(left,right):
    if left<right:
        pivot = hoare_partitional1(left,right)
        quick_sort(left,pivot -1)
        quick_sort(pivot +1 , right)

def hoare_partitional1(left,right):
    pivot = list_A[left]
    i = left +1
    j = right

    while i <= j:
        while i <= j and list_A[i] <=pivot:
            i += 1
        while i <= j and list_A[j] >= pivot:
            j -= 1
        if i < j:
            list_A[i],list_A[j] = list_A[j],list_A[i]

    list_A[left], list_A[j] = list_A[j], list_A[left]
    return j

T= int(input())
for tc in range(1,T+1):
    N = int(input())
    list_A = list(map(int,input().split()))

    quick_sort(0, N -1)
    result = list_A[N //2]
    print(f'#{tc} {result}')