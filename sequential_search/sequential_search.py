
###순차 검색 대상이 정렬되어 있지 않은 경우###
"""
sequentail_search(a, n, key)
    i <- 
    while i<n and a[i]! = key :
            i <- i+1
    if i <n : return 
    else: retrun -1

"""

def sequential_search(a, n, key):
    i = 0
    while i < n and a[i] != key: #어디서 멈췄는지가 관건!! 만약 범위안에서 멈춘거라면 값을 찾은거니까
        i = i + 1
    if i < n:       #배열 범위 안에서 멈췄다면
        return i    # 찾은 위치 반환
    else:           #배열 범위를 벗어났다면
        return -1   # 못찾았다 -1 반환

# 사용 예시
arr = [3, 7, 2, 9, 1]
result = sequential_search(arr, 5, 9)


###순차 검색 대상이 정렬되어 있지 않은 경우에는
찾고자 하는 원소의 순서에 따라 비교회수가 결정됨
평균 비교 횟수 = (1/n) * (1+2+3+....+n) = (n+1)/2
검색 실패시 마지막 원소까지 비교하므로 평균 비교 횟수 n
시간 복잡도 : O(n)