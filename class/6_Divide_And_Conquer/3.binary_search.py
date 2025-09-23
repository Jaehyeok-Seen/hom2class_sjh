def binary_search_while(target):
    left = 0                # 검색 시작점
    right = len(arr) - 1    # 검색 끝점
    cnt = 0                 # 몇 번 만에 검색했는가 ?

    while left <= right:  # 교차되면 못찾은 것
        mid = (left + right) // 2
        cnt += 1  # 검색횟수 추가

        if arr[mid] == target:
            return mid, cnt  # mid 위치에 존재한다고 return

        # target 보다 정답이 왼쪽에 있는 경우
        if target < arr[mid]:
            right = mid - 1
        # target 보다 정답이 오른쪽에 있는 경우
        else:
            left = mid + 1

    # 못찾은 경우
    return -1, cnt

# [참고] 이진 검색 재귀 호출
def binary_search_recur(left, right, target):
    # left, right 를 작업 영역으로 검색
    # left <= right 만족하면 반복
    if left > right:
        return -1

    mid = (left + right) // 2
    # 검색하면 종료
    if target == arr[mid]:
        return mid

    # 한 번 할 때마다 left 와 right 를 mid 기준으로 이동시켜 주면서 진행
    # 왼쪽을 봐야한다
    if target < arr[mid]:
        return binary_search_recur(left, mid - 1, target)
    # 오른쪽을 봐야한다.
    else:
        return binary_search_recur(mid + 1, right, target)


arr = [4, 2, 9, 7, 11, 23, 19]

# 이진 검색은 항상 정렬된 데이터에 적용
arr.sort()  # 2 4 7 9 11 19 23

print(f'9 = {binary_search_while(9)}번째에 위치')
print(f'4 = {binary_search_while(4)}번째에 위치')
print(f'20 = {binary_search_while(20)}번째에 위치')
